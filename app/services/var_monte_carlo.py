import numpy as np
import pandas as pd
from typing import Dict


def monte_carlo_var(
    prices: pd.Series,
    num_simulations: int = 10000,
    horizon_days: int = 1,
    confidence_level: float = 0.95,
) -> Dict[str, float]:
    """Calcule la Value at Risk (VaR) via simulation Monte Carlo.

    :param prices: Historique des prix de clôture.
    :param num_simulations: Nombre de trajectoires simulées.
    :param horizon_days: Horizon temporel en jours.
    :param confidence_level: Niveau de confiance (entre 0 et 1).
    :return: Dictionnaire contenant la VaR et la distribution simulée.
    """
    returns = prices.pct_change().dropna()
    mu = returns.mean()
    sigma = returns.std()
    last_price = prices.iloc[-1]

    # Simule les prix futurs selon un modèle log-normal
    drift = (mu - 0.5 * sigma ** 2) * horizon_days
    diffusion = sigma * np.sqrt(horizon_days) * np.random.randn(num_simulations)
    simulated_prices = last_price * np.exp(drift + diffusion)

    # Pertes (positive si perte)
    losses = last_price - simulated_prices
    var = np.percentile(losses, (1 - confidence_level) * 100)
    return {"VaR": var, "losses": losses}

