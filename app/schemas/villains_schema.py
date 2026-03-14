from pydantic import BaseModel
from typing import List


class Villain(BaseModel):
    name: str
    goal: str


class HeroSummary(BaseModel):
    id: int
    name: str
    age: int
    city: str

    class Config:
        from_attributes = True


class VillainWithHeroes(BaseModel):
    id: int
    name: str
    goal: str
    heroes: List[HeroSummary] = []

    class Config:
        from_attributes = True
