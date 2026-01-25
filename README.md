# Pair Trading Strategy – AAPL / MSFT

## Context

This project explores a basic pair trading strategy based on the spread and z-score between two stocks.

## Objective

The goal is to implement a simple statistical arbitrage strategy and evaluate its performance using historical market data.

## Methodology

- Download historical prices using yfinance
- Compute the price spread between the two assets
- Normalize the spread using a z-score
- Define entry and exit rules based on threshold values
- Backtest the strategy over the year 2023

## Results

The strategy shows periods of profitability when the spread reverts to its mean, illustrating the core intuition behind pair trading.

![Spread and Z-score](figures/spread_zscore.png)
![Cumulative Returns](figures/cumulative_returns.png)

## Limitations

- No transaction costs are considered
- The spread is defined as a simple price difference
- No statistical test (e.g. cointegration) is performed

## Possible Improvements

- Hedge ratio estimation
- Risk management rules
- More robust statistical validation