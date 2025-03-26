from fastapi import HTTPException
from sqlalchemy.orm import Session


from app.repositories.models.heroes_model import HeroModel

class HeroesRepository:

    def get_heroes(self, db: Session):
        return db.query(HeroModel).all()

    def get_hero(self, db: Session, hero_id: int):
        hero = db.query(HeroModel).filter_by(id=hero_id).first()
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        return hero

    def create_hero(self, db: Session, hero: HeroModel):
        new_hero = HeroModel(
        name=hero.name,
        age=hero.age,
        city=hero.city
        )
        db.add(new_hero)
        db.commit()
        db.refresh(new_hero)
        return new_hero

    def update_hero(self, db: Session, hero_id: int, hero: HeroModel):
        db_hero = db.query(HeroModel).filter_by(id=hero_id).first()
        if not db_hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        if db_hero:
            db_hero.name = hero.name
            db_hero.age = hero.age
            db_hero.city = hero.city
        db.commit()
        db.refresh(db_hero)
        return db_hero

    def delete_hero(self, db: Session, hero_id: int):
        db_superhero = db.query(HeroModel).filter(HeroModel.id == hero_id).first()
        if db_superhero:
            db.delete(db_superhero)
            db.commit()
        return db_superhero
