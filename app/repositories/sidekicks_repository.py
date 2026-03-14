from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.models.sidekicks_model import SidekickModel


class SidekicksRepository:

    def get_sidekicks(self, db: Session):
        return db.query(SidekickModel).all()

    def get_sidekick(self, db: Session, sidekick_id: int):
        sidekick = db.query(SidekickModel).filter_by(id=sidekick_id).first()
        if not sidekick:
            raise HTTPException(status_code=404, detail="Sidekick not found")
        return sidekick

    def get_sidekicks_by_hero(self, db: Session, hero_id: int):
        return db.query(SidekickModel).filter_by(hero_id=hero_id).all()

    def create_sidekick(self, db: Session, sidekick: SidekickModel):
        new_sidekick = SidekickModel(
            hero_id=sidekick.hero_id,
            name=sidekick.name,
            superpower=sidekick.superpower
        )
        db.add(new_sidekick)
        db.commit()
        db.refresh(new_sidekick)
        return new_sidekick

    def update_sidekick(self, db: Session, sidekick_id: int, sidekick: SidekickModel):
        db_sidekick = db.query(SidekickModel).filter_by(id=sidekick_id).first()
        if not db_sidekick:
            raise HTTPException(status_code=404, detail="Sidekick not found")
        db_sidekick.hero_id = sidekick.hero_id
        db_sidekick.name = sidekick.name
        db_sidekick.superpower = sidekick.superpower
        db.commit()
        db.refresh(db_sidekick)
        return db_sidekick

    def delete_sidekick(self, db: Session, sidekick_id: int):
        db_sidekick = db.query(SidekickModel).filter(SidekickModel.id == sidekick_id).first()
        if db_sidekick:
            db.delete(db_sidekick)
            db.commit()
        return db_sidekick
