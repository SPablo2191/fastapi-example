from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.repositories.database import Base

class HeroModel(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    city = Column(String, index=True)

    sidekicks = relationship("SidekickModel", back_populates="hero")