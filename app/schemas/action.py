from pydantic import BaseModel
from datetime import date

class ActionBase(BaseModel):
    ticker: str
    nom: str
    devise: str
    quantite: int
    prix_achat: float
    swap_rate: float = 0.0
    date_achat: date
    prix_actuel: float | None = None  # Nouveau
    swap: float = 0.0
class ActionCreate(ActionBase):
    pass

class ActionOut(ActionBase):
    id: int
    class Config:
        from_attributes = True

class ActionFullOut(ActionOut):
    current_price: float | None = None
    gain_eur: float | None = None
    gain_percent: float | None = None
    swap_total: float | None = None
    gain_net: float | None = None
