# La Liga Season 24/25 Simulation

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

| Team            | Avg Rank | Win Probability | 2nd Place Probability | 3rd Place Probability | Top 4 Probability | Bottom Half Probability | Relegation Probability |
|----------------|---------|----------------|-----------------------|-----------------------|------------------|------------------------|-----------------------|
| Real Madrid    | 1.61    | 57.37%         | 26.73%                | 13.53%                | 99.80%           | 0.00%                   | 0.00%                 |
| Barcelona      | 2.34    | 21.66%         | 35.13%                | 32.98%                | 97.90%           | 0.00%                   | 0.00%                 |
| Atletico Madrid | 2.36   | 20.17%         | 34.08%                | 36.70%                | 98.55%           | 0.00%                   | 0.00%                 |
| Athletic Bilbao | 4.40   | 0.70%          | 3.07%                 | 11.70%                | 62.43%           | 0.14%                   | 0.00%                 |
| Villarreal     | 5.35    | 0.08%          | 0.87%                 | 4.22%                 | 29.67%           | 1.44%                   | 0.00%                 |
| Valladolid     | 19.44   | 0.00%          | 0.00%                 | 0.00%                 | 0.00%            | 99.93%                   | 93.23%                 |


## Conclusion
This simulation provides **probabilistic insights** into the final La Liga standings based on team performances. While not a definitive prediction, it offers valuable data-driven expectations for the remainder of the season.

