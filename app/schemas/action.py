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
