from typing import Dict
import pandas as pd
from app.services.yfinance_service import fetch_history
from app.services.var_monte_carlo import monte_carlo_var


def compute_var(ticker: str, num_simulations: int = 10000, horizon_days: int = 1, confidence_level: float = 0.95) -> Dict[str, float]:
    """
    Récupère les prix via yfinance puis calcule la VaR par Monte Carlo.
    """
    # Étape 1: récupération des données historiques
    df: pd.DataFrame = fetch_history(ticker, period="1y")  # utilise yfinance_service
    prices = df['close']
    # Étape 2: calcul de la VaR sur les rendements
    var_result = monte_carlo_var(
        prices,
        num_simulations=num_simulations,
        horizon_days=horizon_days,
        confidence_level=confidence_level
    )
    return var_result