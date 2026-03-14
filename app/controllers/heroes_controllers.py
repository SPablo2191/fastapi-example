from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services import HeroesService
from app.schemas import Hero
from app.schemas.heroes_schema import HeroWithSidekicks

router  = APIRouter(prefix="/heroes", tags=["Heroes"])
service = HeroesService()

@router.get("/hero")
def get_heroes(db: Session = Depends(get_db)):
    return service.get_heroes(db)

@router.get("/hero/{hero_id}", response_model=HeroWithSidekicks)
def get_hero(hero_id: int,db: Session = Depends(get_db),):
    return service.get_hero(db,hero_id)

@router.post("/hero")
def create_hero(hero: Hero,db: Session = Depends(get_db)):
    return service.create_hero(db,hero)

@router.put("/hero/{hero_id}")
def update_hero(hero_id: int, hero: Hero,db: Session = Depends(get_db)):
    return service.update_hero(db,hero_id, hero)


@router.delete("/hero/{hero_id}")
def delete_hero(hero_id: int,db: Session = Depends(get_db)):
    return service.delete_hero(db,hero_id)
