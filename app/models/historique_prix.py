from sqlalchemy import Column, Integer, String, Float, Date, UniqueConstraint
from app.db.base import Base

class HistoriquePrix(Base):
    __tablename__ = "historique_prix"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    date = Column(Date, index=True)
    prix_cloture = Column(Float)

    __table_args__ = (UniqueConstraint("ticker", "date", name="_ticker_date_uc"),)
