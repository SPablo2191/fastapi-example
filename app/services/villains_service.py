from sqlalchemy.orm import Session

from app.repositories import VillainsRepository
from app.repositories.models.villains_model import VillainModel


class VillainsService:
    def __init__(self):
        self.repository: VillainsRepository = VillainsRepository()

    def get_villains(self, db: Session):
        return self.repository.get_villains(db)

    def get_villain(self, db: Session, villain_id: int):
        return self.repository.get_villain(db, villain_id)

    def create_villain(self, db: Session, villain: VillainModel):
        return self.repository.create_villain(db, villain)

    def update_villain(self, db: Session, villain_id: int, villain: VillainModel):
        return self.repository.update_villain(db, villain_id, villain)

    def delete_villain(self, db: Session, villain_id: int):
        return self.repository.delete_villain(db, villain_id)

    def add_hero_to_villain(self, db: Session, villain_id: int, hero_id: int):
        return self.repository.add_hero_to_villain(db, villain_id, hero_id)

    def remove_hero_from_villain(self, db: Session, villain_id: int, hero_id: int):
        return self.repository.remove_hero_from_villain(db, villain_id, hero_id)
