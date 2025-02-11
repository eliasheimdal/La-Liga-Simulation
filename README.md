# La Liga Season 24/25 Simulation

## Overview
This project simulates the remaining fixtures of the **2024/25 La Liga season** to predict the final league standings. The simulation is based on historical data from past seasons and the current standings.

## Data Sources
The simulation uses match data from the following seasons:
- **2021/22**
- **2022/23**
- **2023/24**
- **2024/25** (up to the latest completed matches)

Additionally, the **remaining fixtures** of the 24/25 season are incorporated to simulate potential results.

## Methodology
### **Step 1: Data Preparation**
- All available match data is preprocessed and aggregated.
- The league table is initialized using the latest **24/25 season standings**.
- **Historical match data** is used to compute goal-scoring and defensive strengths for each team.

### **Step 2: Simulation**
- Each remaining match is simulated **10,000 times** using a **Poisson distribution**, which models the expected number of goals for each team based on their historical performance.
- The league table is updated dynamically with each simulated result.

### **Step 3: Statistical Analysis**
After all simulations, the following probabilities are computed for each team:
- **Average Final Ranking**
- **Win Probability** (Chance of winning La Liga)
- **Second Place Probability**
- **Third Place Probability**
- **Top 4 Probability** (Champions League Qualification)
- **Bottom Half Probability**
- **Relegation Probability**

## Results

| Team         | Avg Rank | Win Probability | Second Place Probability | Third Place Probability | Top 4 Probability | Bottom Half Probability | Relegation Probability |
|-------------|----------|----------------|-------------------------|------------------------|------------------|------------------------|----------------------|
| Real Madrid  | 1.6112   | 57.37          | 26.73                   | 13.53                   | 99.80            | 0.00                   | 0.00                 |
| Barcelona    | 2.3448   | 21.66          | 35.13                   | 32.98                   | 97.90            | 0.00                   | 0.00                 |
| Ath Madrid   | 2.3632   | 20.17          | 34.08                   | 36.70                   | 98.55            | 0.00                   | 0.00                 |
| Ath Bilbao   | 4.4063   | 0.70           | 3.07                    | 11.70                   | 62.43            | 0.14                   | 0.00                 |
| Villarreal   | 5.3535   | 0.08           | 0.87                    | 4.22                    | 29.67            | 1.44                   | 0.00                 |
| Girona       | 7.4818   | 0.02           | 0.08                    | 0.52                    | 5.66             | 12.35                  | 0.07                 |
| Vallecano    | 8.9791   | 0.00           | 0.00                    | 0.12                    | 2.03             | 27.10                  | 0.37                 |
| Betis        | 9.6786   | 0.00           | 0.02                    | 0.08                    | 1.13             | 36.55                  | 0.67                 |
| Sociedad     | 9.7091   | 0.00           | 0.00                    | 0.05                    | 1.01             | 36.48                  | 0.89                 |
| Sevilla      | 10.4221  | 0.00           | 0.00                    | 0.03                    | 0.73             | 46.66                  | 1.75                 |
| Osasuna      | 10.6488  | 0.00           | 0.02                    | 0.03                    | 0.55             | 49.71                  | 1.72                 |
| Mallorca     | 10.7871  | 0.00           | 0.00                    | 0.03                    | 0.42             | 51.62                  | 1.69                 |
| Celta        | 13.2716  | 0.00           | 0.00                    | 0.01                    | 0.04             | 79.26                  | 9.74                 |
| Getafe       | 14.1429  | 0.00           | 0.00                    | 0.00                    | 0.06             | 85.67                  | 15.69                |
| Las Palmas   | 15.2099  | 0.00           | 0.00                    | 0.00                    | 0.01             | 92.15                  | 25.45                |
| Espanol      | 15.5663  | 0.00           | 0.00                    | 0.00                    | 0.01             | 93.89                  | 30.19                |
| Leganes      | 15.6214  | 0.00           | 0.00                    | 0.00                    | 0.00             | 93.77                  | 31.27                |
| Alaves       | 16.3272  | 0.00           | 0.00                    | 0.00                    | 0.00             | 96.31                  | 41.18                |
| Valencia     | 16.6301  | 0.00           | 0.00                    | 0.00                    | 0.00             | 96.97                  | 46.09                |
| Valladolid   | 19.4450  | 0.00           | 0.00                    | 0.00                    | 0.00             | 99.93                  | 93.23                |

## Conclusion
This simulation provides **probabilistic insights** into the final La Liga standings based on team performances. While not a definitive prediction, it offers valuable data-driven expectations for the remainder of the season.

# Datasets
Datasets are from https://github.com/datasets/football-datasets

