from app.repositories import HeroesRepository
from app.schemas import Hero    


class HeroesService:
    def __init__(self):
        self.repository : HeroesRepository = HeroesRepository()

    def get_heroes(self):
        return self.repository.get_heroes()

    def get_hero(self, hero_id: int):
        return self.repository.get_hero(hero_id)

    def create_hero(self, hero: Hero):
        return self.repository.create_hero(hero)

    def update_hero(self, hero_id: int, hero: Hero):
        return self.repository.update_hero(hero_id, hero)

    def delete_hero(self, hero_id: int):
        return self.repository.delete_hero(hero_id)