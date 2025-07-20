import yfinance as yf
import pandas as pd


def fetch_history(ticker: str, period: str = "1y") -> pd.DataFrame:
    """
    Récupère l'historique du cours de clôture pour le ticker sur la période donnée.
    """
    data = yf.Ticker(ticker).history(period=period)
    return data[["Close"]].rename(columns={"Close": "close"})


def fetch_current_price(ticker: str) -> float:
    """Récupère le cours de clôture le plus récent"""
    return float(fetch_history(ticker, period="5d")["close"].iloc[-1])