from sqlalchemy import Column, Integer, String, Float, ForeignKey,Date
from sqlalchemy.orm import relationship
from app.db.base import Base


class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    ticker = Column(String, index=True)
    nom = Column(String)
    devise = Column(String)
    quantite = Column(Integer)
    prix_achat = Column(Float)
    prix_actuel = Column(Float, nullable=True)  # Nouveau champ
    swap = Column(Float, default=0.0)           # Nouveau champ
    date_achat = Column(Date)
