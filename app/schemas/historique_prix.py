from pydantic import BaseModel
from datetime import date

class HistoriquePrixOut(BaseModel):
    ticker: str
    date: date
    prix_cloture: float

    class Config:
        from_attributes = True
