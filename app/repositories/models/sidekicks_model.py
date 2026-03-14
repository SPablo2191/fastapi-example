from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.repositories.database import Base


class SidekickModel(Base):
    __tablename__ = "sidekicks"

    id = Column(Integer, primary_key=True, index=True)
    hero_id = Column(Integer, ForeignKey("heroes.id"), nullable=False)
    name = Column(String, index=True)
    superpower = Column(String)

    hero = relationship("HeroModel", back_populates="sidekicks")
