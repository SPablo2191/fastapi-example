from fastapi import HTTPException
from  app.repositories.database import  data
from app.schemas import Hero

class HeroesRepository:
    def __init__(self):
        self.data = data

    def get_heroes(self):
        return self.data

    def get_hero(self, hero_id: int):
        if not hero_id in range(len(self.data)):
            raise HTTPException(status_code=404, detail="Hero not found")
        return self.data[hero_id]

    def create_hero(self, hero: Hero):
        self.data.append(hero.model_dump())
        return self.data[-1]

    def update_hero(self, hero_id: int, hero: Hero):
        if not hero_id in range(len(self.data)):
            raise HTTPException(status_code=404, detail="Hero not found")
        self.data[hero_id] = hero.model_dump()
        return self.data[hero_id]

    def delete_hero(self, hero_id: int):
        if not hero_id in range(len(self.data)):
            raise HTTPException(status_code=404, detail="Hero not found")
        self.data.pop(hero_id)
        return self.data