from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    nom = Column(String)
    devise = Column(String)
    quantite = Column(Integer)
    prix_achat = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Lien avec utilisateur
    user = relationship("User", back_populates="actions")
