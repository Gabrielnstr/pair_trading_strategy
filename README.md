# Pair Trading Strategy – AAPL / MSFT

## Context

This project explores a basic pair trading strategy based on mean reversion between two highly correlated stocks.

## Objective

The goal is to implement a simple statistical arbitrage strategy and evaluate its performance using historical market data.

## Methodology

- Download historical prices using yfinance  
- Compute the spread using **log-prices**  
- Estimate the hedge ratio using **OLS regression**  
- Normalize the spread using a **rolling z-score** (to avoid look-ahead bias)  
- Define entry and exit rules based on threshold values  
- Backtest the strategy over the year 2023  
- Include transaction costs to simulate realistic trading conditions  

## Statistical Validation

An Engle-Granger cointegration test was performed to assess the long-term relationship between the assets.

The test yields a p-value of approximately 0.042, indicating statistical significance at the 5% level. However, the relationship remains relatively weak and may not persist across different time periods.

## Performance

### Gross Performance (before costs)

- **Sharpe Ratio:** 1.24  
- **Cumulative Return:** 18.93%  

### Net Performance (after transaction costs)

- **Sharpe Ratio:** 0.87  
- **Cumulative Return:** 13.03%  
- **Volatility:** 15.10%  
- **Max Drawdown:** -8.42%  

The strategy remains profitable after including transaction costs, indicating a certain level of robustness. However, performance is significantly reduced, highlighting the impact of trading frictions.

## Results

The spread shows mean-reverting behavior, generating trading opportunities when extreme deviations occur.

The comparison between gross and net returns highlights the importance of accounting for transaction costs when evaluating trading strategies.

![Spread and Z-score](figures/spread_zscore.png)
![Cumulative Returns](figures/cumulative_returns.png)
![Drawdown](figures/drawdown.png)

## Limitations

- Transaction costs are simplified and assumed constant over time  
- Cointegration is statistically significant but relatively weak  
- Strategy tested on a single time period (no out-of-sample validation)  
- Simplified model assumptions despite hedge ratio estimation  

## Possible Improvements

- Perform cointegration tests over multiple periods  
- Use dynamic (rolling) hedge ratio  
- Add more realistic transaction cost modeling  
- Implement risk management (position sizing, stop-loss)  
- Perform out-of-sample and walk-forward testing  