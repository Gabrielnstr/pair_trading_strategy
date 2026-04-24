import pandas as pd

def compute_zscore(series: pd.Series, window: int = 20) -> pd.Series:
    rolling_mean = series.rolling(window).mean()
    rolling_std = series.rolling(window).std(ddof=0)
    
    zscore = (series - rolling_mean) / rolling_std
    
    return zscore
