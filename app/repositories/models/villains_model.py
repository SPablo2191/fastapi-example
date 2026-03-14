from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.repositories.database import Base

# Association table for many-to-many: heroes <-> villains
hero_villain = Table(
    "hero_villain",
    Base.metadata,
    Column("hero_id", Integer, ForeignKey("heroes.id"), primary_key=True),
    Column("villain_id", Integer, ForeignKey("villains.id"), primary_key=True),
)


class VillainModel(Base):
    __tablename__ = "villains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    goal = Column(String)

    heroes = relationship("HeroModel", secondary=hero_villain, back_populates="villains")
