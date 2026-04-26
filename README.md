# Pair Trading Strategy – AAPL / MSFT

## Context

This project explores a basic pair trading strategy based on mean reversion between two highly correlated stocks.

## Objective

The goal is to implement a simple statistical arbitrage strategy and evaluate its performance using historical market data.

## Methodology

- Download historical prices using yfinance
- Compute the spread using **log-prices**
- Normalize the spread using a **rolling z-score** (to avoid look-ahead bias)
- Define entry and exit rules based on threshold values
- Backtest the strategy over the year 2023

## Statistical Validation

An Engle-Granger cointegration test was performed to assess the long-term relationship between the assets.
The test yields a p-value of approximately 0.042, indicating statistical significance at the 5% level. However, the relationship remains relatively weak and may not persist across different time periods.

## Performance

- **Sharpe Ratio:** 1.87
- **Cumulative Return:** 29.49%
- **Volatility:** 15.96%
- **Max Drawdown:** -11.34%

The strategy exhibits strong risk-adjusted performance over the selected period.
These results suggest that the strategy captures short-term mean reversion effects, although performance may be overstated due to model simplifications.

## Results

The spread shows mean-reverting behavior, generating trading opportunities when extreme deviations occur.

![Spread and Z-score](figures/spread_zscore.png)
![Cumulative Returns](figures/cumulative_returns.png)

## Limitations

- No transaction costs or slippage
- Cointegration is statistically significant, but remains relatively weak and may not be stable over time
- Simplified spread model (no hedge ratio)
- Strategy tested on a single time period (no out-of-sample validation)

## Possible Improvements

- Estimate hedge ratio using regression
- Perform cointegration test on multiple periods
- Add transaction costs and slippage
- Implement risk management
- Perform out-of-sample and walk-forward testing