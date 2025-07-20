import numpy as np
import pandas as pd


def compute_kpis(prices: pd.Series) -> dict:
    returns = prices.pct_change().dropna()
    mean_ret = returns.mean() * 252
    vol = returns.std() * np.sqrt(252)
    sharpe = mean_ret / vol if vol != 0 else None
    return {"annual_return": mean_ret, "volatility": vol, "sharpe_ratio": sharpe}

