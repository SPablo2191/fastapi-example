from pydantic import BaseModel
from typing import List


class Hero(BaseModel):
    name: str
    age: int
    city: str


class SidekickResponse(BaseModel):
    id: int
    name: str
    superpower: str

    class Config:
        from_attributes = True


class VillainSummary(BaseModel):
    id: int
    name: str
    goal: str

    class Config:
        from_attributes = True


class HeroWithSidekicks(BaseModel):
    id: int
    name: str
    age: int
    city: str
    sidekicks: List[SidekickResponse] = []
    villains: List[VillainSummary] = []

    class Config:
        from_attributes = True