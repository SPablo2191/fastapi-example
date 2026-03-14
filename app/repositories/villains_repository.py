from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from app.repositories.models.villains_model import VillainModel
from app.repositories.models.heroes_model import HeroModel


class VillainsRepository:

    def get_villains(self, db: Session):
        return db.query(VillainModel).all()

    def get_villain(self, db: Session, villain_id: int):
        villain = db.query(VillainModel).options(joinedload(VillainModel.heroes)).filter_by(id=villain_id).first()
        if not villain:
            raise HTTPException(status_code=404, detail="Villain not found")
        return villain

    def create_villain(self, db: Session, villain: VillainModel):
        new_villain = VillainModel(
            name=villain.name,
            goal=villain.goal
        )
        db.add(new_villain)
        db.commit()
        db.refresh(new_villain)
        return new_villain

    def update_villain(self, db: Session, villain_id: int, villain: VillainModel):
        db_villain = db.query(VillainModel).filter_by(id=villain_id).first()
        if not db_villain:
            raise HTTPException(status_code=404, detail="Villain not found")
        db_villain.name = villain.name
        db_villain.goal = villain.goal
        db.commit()
        db.refresh(db_villain)
        return db_villain

    def delete_villain(self, db: Session, villain_id: int):
        db_villain = db.query(VillainModel).filter(VillainModel.id == villain_id).first()
        if db_villain:
            db.delete(db_villain)
            db.commit()
        return db_villain

    def add_hero_to_villain(self, db: Session, villain_id: int, hero_id: int):
        villain = db.query(VillainModel).options(joinedload(VillainModel.heroes)).filter_by(id=villain_id).first()
        if not villain:
            raise HTTPException(status_code=404, detail="Villain not found")
        hero = db.query(HeroModel).filter_by(id=hero_id).first()
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        if hero not in villain.heroes:
            villain.heroes.append(hero)
            db.commit()
            db.refresh(villain)
        return villain

    def remove_hero_from_villain(self, db: Session, villain_id: int, hero_id: int):
        villain = db.query(VillainModel).options(joinedload(VillainModel.heroes)).filter_by(id=villain_id).first()
        if not villain:
            raise HTTPException(status_code=404, detail="Villain not found")
        hero = db.query(HeroModel).filter_by(id=hero_id).first()
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        if hero in villain.heroes:
            villain.heroes.remove(hero)
            db.commit()
            db.refresh(villain)
        return villain
