from pydantic import BaseModel

class ActionBase(BaseModel):
    ticker: str
    nom: str
    devise: str
    quantite: int
    prix_achat: float

class ActionCreate(ActionBase):
    pass

class ActionOut(ActionBase):
    id: int

    class Config:
        from_attributes = True  # nouvelle syntaxe Pydantic v2

class ActionFullOut(ActionOut):
    current_price: float | None = None
    gain_eur: float | None = None
    gain_percent: float | None = None

    class Config:
        from_attributes = True