Commodity Market Simulation Using NumPy

A simple Python project that simulates the price movement of selected commodities over a one-year period using random market fluctuations and basic economic events.

This project was built to practice working with NumPy arrays, simulation modeling, data analysis, and Matplotlib visualizations while exploring how external events can influence commodity prices.

Overview

The simulation tracks four commodities:

Gold
Silver
Oil
Wheat

Prices change daily based on:

Random market fluctuations
Inflation events
Recession events
War events

At the end of the simulation, the program:

Calculates percentage growth for each commodity
Displays final performance statistics
Visualizes price trends using Matplotlib charts
Features
Daily Market Movement

Each commodity experiences random daily returns generated from a normal distribution:

Mean daily return: 0.1%
Volatility: 2%

This creates realistic-looking price variations over time.

Economic Event Simulation

Random economic events may occur during the simulation:

Event	Effect
Inflation	Increases Gold and Oil prices
Recession	Reduces Silver and Oil prices
War	Strongly increases Gold and Oil prices

These events introduce sudden market shocks and demonstrate how external factors can influence asset performance.

Performance Analysis

After 365 simulated days, the program calculates:

Initial price
Final price
Total percentage growth

for each commodity.

Visualization

The project generates individual charts showing the price history of:

Gold
Silver
Oil
Wheat

This makes it easier to observe long-term trends and event-driven changes.

Technologies Used
Python
NumPy
Matplotlib
Project Structure
commodity_market_simulation.py

├── Commodity initialization
├── Economic event functions
│   ├── inflation()
│   ├── recession()
│   └── war()
├── Daily simulation loop
├── Growth calculation
├── Results summary
└── Visualization
Example Output
Day 42: Inflation Crisis
Day 97: Recession Crisis
Day 214: War Crisis

Gold: $4500.00 -> $5231.42 (16.25%)
Silver: $76.00 -> $81.67 (7.46%)
Oil: $96.00 -> $118.50 (23.44%)
Wheat: $6.00 -> $6.42 (7.00%)

Results vary on each run because of randomness.

Learning Objectives

This project helped explore:

NumPy array operations
Random number generation
Simulation-based modeling
Basic financial market concepts
Data visualization with Matplotlib
Function-based program organization
Limitations

This project is intended for educational purposes and does not represent real commodity market behavior.

Some simplifications include:

Fixed event probabilities
Simplified economic impacts
No supply-demand modeling
No historical market data
Independent asset behavior

Real-world commodity markets are influenced by many additional factors including geopolitical events, monetary policy, weather conditions, production levels, and investor sentiment.

Future Improvements

Possible enhancements include:

Using real historical commodity data
Correlated asset movements
Dynamic event severity
Supply and demand modeling
Monte Carlo simulations
Risk metrics and portfolio analysis
Interactive dashboards
More advanced visualizations
Disclaimer

This project is a learning exercise focused on simulation techniques using Python, NumPy, and Matplotlib. The generated results should not be used for financial decision-making or investment advice.

Author

Banty Kumar

Built as a practice project to strengthen understanding of NumPy-based simulations, market modeling concepts, and data visualization in Python
