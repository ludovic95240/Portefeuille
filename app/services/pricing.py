import yfinance as yf
from datetime import date
from sqlalchemy.orm import Session
from app.models.historique_prix import HistoriquePrix

def fetch_and_store_history(db: Session, ticker: str, start: date, end: date):
    df = yf.download(ticker, start=start.isoformat(), end=end.isoformat())
    for index, row in df.iterrows():
        hp = HistoriquePrix(
            ticker=ticker,
            date=index.date(),
            prix_cloture=row["Close"]
        )
        db.merge(hp)
    db.commit()
    return len(df)

def get_history(db: Session, ticker: str, start: date, end: date):
    return db.query(HistoriquePrix)\
        .filter(HistoriquePrix.ticker == ticker,
                HistoriquePrix.date >= start,
                HistoriquePrix.date <= end)\
        .order_by(HistoriquePrix.date).all()
