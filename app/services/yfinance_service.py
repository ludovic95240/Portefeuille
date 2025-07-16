import yfinance as yf

def get_current_price(ticker: str) -> float:
    try:
        data = yf.Ticker(ticker)
        hist = data.history(period="1d")
        return float(hist["Close"].iloc[-1])
    except Exception as e:
        print(f"[YF ERROR] {ticker} : {e}")
        return None
