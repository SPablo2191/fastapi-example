from sqlalchemy.orm import Session

from app.repositories import HeroesRepository
from app.repositories.models.heroes_model import HeroModel   


class HeroesService:
    def __init__(self):
        self.repository : HeroesRepository = HeroesRepository()

    def get_heroes(self, db: Session):
        return self.repository.get_heroes(db)

    def get_hero(self, db: Session, hero_id: int):
        return self.repository.get_hero(db,hero_id)

    def create_hero(self, db: Session, hero: HeroModel):
        return self.repository.create_hero(db,hero)

    def update_hero(self, db: Session, hero_id: int, hero: HeroModel):
        return self.repository.update_hero(db,hero_id, hero)

    def delete_hero(self, db: Session, hero_id: int):
        return self.repository.delete_hero(db,hero_id)