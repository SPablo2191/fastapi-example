from sqlalchemy.orm import Session

from app.repositories import SidekicksRepository
from app.repositories.models.sidekicks_model import SidekickModel


class SidekicksService:
    def __init__(self):
        self.repository: SidekicksRepository = SidekicksRepository()

    def get_sidekicks(self, db: Session):
        return self.repository.get_sidekicks(db)

    def get_sidekick(self, db: Session, sidekick_id: int):
        return self.repository.get_sidekick(db, sidekick_id)

    def get_sidekicks_by_hero(self, db: Session, hero_id: int):
        return self.repository.get_sidekicks_by_hero(db, hero_id)

    def create_sidekick(self, db: Session, sidekick: SidekickModel):
        return self.repository.create_sidekick(db, sidekick)

    def update_sidekick(self, db: Session, sidekick_id: int, sidekick: SidekickModel):
        return self.repository.update_sidekick(db, sidekick_id, sidekick)

    def delete_sidekick(self, db: Session, sidekick_id: int):
        return self.repository.delete_sidekick(db, sidekick_id)
