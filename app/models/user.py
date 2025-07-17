from sqlalchemy import Column, Integer, String
from app.db.base import Base

from sqlalchemy.orm import relationship
# ...



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    actions = relationship("Action", back_populates="user")