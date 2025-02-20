# La Liga Season 24/25 Simulation (Updated Feb 20)

## Overview
This project simulates the remaining fixtures of the **2024/25 La Liga season** to predict the final league standings. The simulation is based on historical data from past seasons and the current standings.

## Data Sources
The simulation uses match data from the following seasons:
- **2020/21**
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
|------------|----------|-----------------|---------------------------|-------------------------|-------------------|-------------------------|------------------------|
| Real Madrid  | 1.8443   | 42.47%          | 34.72%                    | 19.03%                  | 99.69%            | 0.00%                   | 0.00%                  |
| Barcelona   | 1.8930   | 41.70%          | 32.85%                    | 20.72%                  | 99.28%            | 0.00%                   | 0.00%                  |
| Ath Madrid  | 2.5738   | 14.97%          | 28.51%                    | 43.20%                  | 97.75%            | 0.00%                   | 0.00%                  |
| Ath Bilbao  | 4.1930   | 0.75%           | 3.16%                     | 12.72%                  | 69.43%            | 0.03%                   | 0.00%                  |
| Villarreal  | 5.1400   | 0.11%           | 0.76%                     | 4.06%                   | 29.24%            | 0.78%                   | 0.00%                  |
| Vallecano   | 8.7837   | 0.00%           | 0.00%                     | 0.09%                   | 1.24%             | 26.21%                  | 0.12%                  |
| Girona      | 9.2274   | 0.00%           | 0.00%                     | 0.05%                   | 0.72%             | 31.33%                  | 0.31%                  |
| Betis       | 9.4302   | 0.00%           | 0.00%                     | 0.06%                   | 0.70%             | 34.17%                  | 0.24%                  |
| Sociedad    | 9.9283   | 0.00%           | 0.00%                     | 0.01%                   | 0.65%             | 41.60%                  | 0.48%                  |
| Sevilla     | 10.1537  | 0.00%           | 0.00%                     | 0.02%                   | 0.54%             | 44.06%                  | 0.67%                  |
| Mallorca    | 10.2434  | 0.00%           | 0.00%                     | 0.02%                   | 0.36%             | 45.62%                  | 0.47%                  |
| Osasuna     | 10.8628  | 0.00%           | 0.00%                     | 0.00%                   | 0.25%             | 54.09%                  | 0.93%                  |
| Getafe      | 11.6648  | 0.00%           | 0.00%                     | 0.02%                   | 0.10%             | 64.06%                  | 2.37%                  |
| Celta       | 12.1717  | 0.00%           | 0.00%                     | 0.00%                   | 0.04%             | 70.19%                  | 3.14%                  |
| Valencia    | 15.7635  | 0.00%           | 0.00%                     | 0.00%                   | 0.01%             | 95.82%                  | 27.77%                 |
| Espanol     | 16.3087  | 0.00%           | 0.00%                     | 0.00%                   | 0.00%             | 97.08%                  | 36.81%                 |
| Leganes     | 16.5067  | 0.00%           | 0.00%                     | 0.00%                   | 0.00%             | 97.96%                  | 40.22%                 |
| Las Palmas  | 16.5506  | 0.00%           | 0.00%                     | 0.00%                   | 0.00%             | 98.07%                  | 40.11%                 |
| Alaves      | 17.0341  | 0.00%           | 0.00%                     | 0.00%                   | 0.00%             | 98.93%                  | 49.09%                 |
| Valladolid  | 19.7263  | 0.00%           | 0.00%                     | 0.00%                   | 0.00%             | 100.00%                 | 97.27%                 |


## Conclusion
This simulation provides **probabilistic insights** into the final La Liga standings based on team performances. While not a definitive prediction, it offers valuable data-driven expectations for the remainder of the season.

# Datasets
Datasets are from https://github.com/datasets/football-datasets

