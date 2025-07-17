# app/services/yfinance_service.py
import yfinance as yf

def get_current_price(ticker: str) -> float | None:
    try:
        data = yf.Ticker(ticker)
        hist = data.history(period="1d")
        return float(hist["Close"].iloc[-1])
    except Exception as e:
        print(f"Erreur YFinance pour {ticker} : {e}")
        return None
