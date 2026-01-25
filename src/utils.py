import pandas as pd

def compute_zscore(series: pd.Series) -> pd.Series:
    """
    Compute the z-score of a pandas Series.

    Parameters
    ----------
    series : pd.Series
        Input time series (e.g. spread between two assets)

    Returns
    -------
    pd.Series
        Z-score normalized series
    """
    mean = series.mean()
    std = series.std()
    zscore = (series - mean) / std
    return zscore
