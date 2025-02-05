import pandas as pd
import numpy as np
from scipy.stats import poisson

# Load historical and current season data
df_2021 = pd.read_csv('season-2021.csv', encoding='utf-8')
df_2122 = pd.read_csv('season-2122.csv', encoding='utf-8')
df_2223 = pd.read_csv('season-2223.csv', encoding='utf-8')
df_2324 = pd.read_csv('season-2324.csv', encoding='utf-8')
df_2425 = pd.read_csv('season-2425.csv', encoding='utf-8')
df_fixtures = pd.read_csv('remaining-fixtures.csv', encoding='utf-8')

# Preprocess Date Columns
df_2021['Date'] = pd.to_datetime(df_2021['Date'], format='%d/%m/%y')
df_2122['Date'] = pd.to_datetime(df_2122['Date'], format='%d/%m/%y')
df_2223['Date'] = pd.to_datetime(df_2223['Date'], format='%d/%m/%y')
df_2324['Date'] = pd.to_datetime(df_2324['Date'], format='%d/%m/%y')
df_2425['Date'] = pd.to_datetime(df_2425['Date'], format='%d/%m/%y')
df_fixtures['Date'] = pd.to_datetime(df_fixtures['Date'], format='%d/%m/%Y %H:%M')

# Create df_all for training (combining past and current season data)
df_all = pd.concat([df_2021 ,df_2122 ,df_2223 ,df_2324, df_2425], ignore_index=True)

# Compute goal-scoring and conceding averages from df_all
team_stats_all = df_all.groupby('HomeTeam').agg(
    home_goals_scored=('FTHG', 'mean'),
    home_goals_conceded=('FTAG', 'mean')
).reset_index().rename(columns={'HomeTeam': 'Team'})

away_stats_all = df_all.groupby('AwayTeam').agg(
    away_goals_scored=('FTAG', 'mean'),
    away_goals_conceded=('FTHG', 'mean')
).reset_index().rename(columns={'AwayTeam': 'Team'})

team_stats_all = pd.merge(team_stats_all, away_stats_all, on='Team', how='outer').fillna(0)

# Compute current league standings ONLY from season-2425.csv
teams = {}
for _, row in df_2425.iterrows():
    home_team, away_team = row['HomeTeam'], row['AwayTeam']
    home_goals, away_goals = row['FTHG'], row['FTAG']
    result = row['FTR']
    
    for team in [home_team, away_team]:
        if team not in teams:
            teams[team] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'GF': 0, 'GA': 0, 'GD': 0, 'Pts': 0}
    
    teams[home_team]['MP'] += 1
    teams[away_team]['MP'] += 1
    
    teams[home_team]['GF'] += home_goals
    teams[home_team]['GA'] += away_goals
    teams[away_team]['GF'] += away_goals
    teams[away_team]['GA'] += home_goals
    
    if result == 'H':
        teams[home_team]['W'] += 1
        teams[away_team]['L'] += 1
        teams[home_team]['Pts'] += 3
    elif result == 'A':
        teams[away_team]['W'] += 1
        teams[home_team]['L'] += 1
        teams[away_team]['Pts'] += 3
    elif result == 'D':
        teams[home_team]['D'] += 1
        teams[away_team]['D'] += 1
        teams[home_team]['Pts'] += 1
        teams[away_team]['Pts'] += 1

for team in teams:
    teams[team]['GD'] = teams[team]['GF'] - teams[team]['GA']

team_stats = pd.DataFrame.from_dict(teams, orient='index')
team_stats.index.name = 'Team'
team_stats = team_stats.reset_index()

# Merge training stats with current standings
team_stats = team_stats.merge(team_stats_all, on='Team', how='left').fillna(0)

# Dictionary for quick lookup
goal_stats = team_stats.set_index('Team').to_dict(orient='index')

# Initialize standings with current league standings
standings_simulations = {team: [] for team in team_stats['Team']}

def simulate_match(home_team, away_team):
    home_attack = goal_stats[home_team]['home_goals_scored']
    away_defense = goal_stats[away_team]['away_goals_conceded']
    away_attack = goal_stats[away_team]['away_goals_scored']
    home_defense = goal_stats[home_team]['home_goals_conceded']
    
    home_goals = poisson.rvs((home_attack + away_defense) / 2)
    away_goals = poisson.rvs((away_attack + home_defense) / 2)
    
    if home_goals > away_goals:
        return home_team, 3, home_goals - away_goals
    elif home_goals < away_goals:
        return away_team, 3, away_goals - home_goals
    else:
        return None, 1, 0

def run_simulations(n=10000):
    for _ in range(n):
        print(f"Simulation {_ + 1}/{n}", end='\r')
        table = {team: {'points': goal_stats[team]['Pts'], 'goal_difference': goal_stats[team]['GD']} for team in team_stats['Team']}
        for _, row in df_fixtures.iterrows():
            winner, points, goal_diff = simulate_match(row['HomeTeam'], row['AwayTeam'])
            if winner:
                table[winner]['points'] += points
                table[winner]['goal_difference'] += goal_diff
            else:
                table[row['HomeTeam']]['points'] += 1
                table[row['AwayTeam']]['points'] += 1
        
        sorted_teams = sorted(table.items(), key=lambda x: (-x[1]['points'], -x[1]['goal_difference']))
        for rank, (team, stats) in enumerate(sorted_teams, start=1):
            standings_simulations[team].append(rank)

    final_results = []
    for team, ranks in standings_simulations.items():
        avg_rank = np.mean(ranks)
        win_prob = np.mean(np.array(ranks) == 1) * 100
        second_prob = np.mean(np.array(ranks) == 2) * 100
        third_prob = np.mean(np.array(ranks) == 3) * 100
        top4_prob = np.mean(np.array(ranks) <= 4) * 100
        bottomhalf_prob = np.mean(np.array(ranks) >= 11) * 100
        relegation_prob = np.mean(np.array(ranks) >= 18) * 100
        final_results.append([team, avg_rank, win_prob, second_prob, third_prob, top4_prob, bottomhalf_prob,relegation_prob])
    
    final_df = pd.DataFrame(final_results, columns=['Team', 'Avg Rank', 'Win Probability', 'Second Place Probability', 'Third Place Probability', 'Top 4 Probability', 'Bottom Half Probability', 'Relegation Probability'])
    final_df.sort_values(by='Avg Rank', inplace=True)
        
    print("Final League Predictions")
    print(final_df)

# Run 10,000 simulations
run_simulations(10000)
