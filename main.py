import pandas as pd

# Read the CSV file using the default delimiter (comma).
df = pd.read_csv('season-2425.csv', encoding='utf-8')

# Debug: print the column names to verify they are read correctly.
print("Columns found:", df.columns.tolist())

# Remove any potential leading/trailing whitespace from the column names.
df.columns = df.columns.str.strip()

# Verify again (optional)
print("Columns after stripping whitespace:", df.columns.tolist())

# Create an empty dictionary to store each team's statistics.
teams = {}

# Process each match to update the league table.
for index, row in df.iterrows():
    # Extract relevant match information.
    home_team = row['HomeTeam']
    away_team = row['AwayTeam']
    home_goals = row['FTHG']
    away_goals = row['FTAG']
    result = row['FTR']  # Full Time Result ('H', 'D', or 'A')
    
    # Ensure both teams are in our dictionary; initialize if not present.
    for team in [home_team, away_team]:
        if team not in teams:
            teams[team] = {
                'MP': 0,  # Matches Played
                'W': 0,   # Wins
                'D': 0,   # Draws
                'L': 0,   # Losses
                'GF': 0,  # Goals For
                'GA': 0,  # Goals Against
                'GD': 0,  # Goal Difference
                'Pts': 0  # Points
            }
    
    # Increment matches played.
    teams[home_team]['MP'] += 1
    teams[away_team]['MP'] += 1
    
    # Update goals scored and conceded.
    teams[home_team]['GF'] += home_goals
    teams[home_team]['GA'] += away_goals
    teams[away_team]['GF'] += away_goals
    teams[away_team]['GA'] += home_goals
    
    # Update wins, draws, losses, and points based on the match result.
    if result == 'H':  # Home win
        teams[home_team]['W'] += 1
        teams[away_team]['L'] += 1
        teams[home_team]['Pts'] += 3
    elif result == 'A':  # Away win
        teams[away_team]['W'] += 1
        teams[home_team]['L'] += 1
        teams[away_team]['Pts'] += 3
    elif result == 'D':  # Draw
        teams[home_team]['D'] += 1
        teams[away_team]['D'] += 1
        teams[home_team]['Pts'] += 1
        teams[away_team]['Pts'] += 1

# After processing all matches, calculate goal difference for each team.
for team in teams:
    teams[team]['GD'] = teams[team]['GF'] - teams[team]['GA']

# Convert the teams dictionary into a DataFrame for easy manipulation and display.
league_table = pd.DataFrame.from_dict(teams, orient='index')
league_table.index.name = 'Team'

# Sort the table by Points, then Goal Difference, then Goals For.
league_table = league_table.sort_values(by=['Pts', 'GD', 'GF'], ascending=False)

# Display the league table.
print(league_table)
