from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services import VillainsService
from app.schemas import Villain
from app.schemas.villains_schema import VillainWithHeroes

router = APIRouter(prefix="/villains", tags=["Villains"])
service = VillainsService()


@router.get("/villain")
def get_villains(db: Session = Depends(get_db)):
    return service.get_villains(db)


@router.get("/villain/{villain_id}", response_model=VillainWithHeroes)
def get_villain(villain_id: int, db: Session = Depends(get_db)):
    return service.get_villain(db, villain_id)


@router.post("/villain")
def create_villain(villain: Villain, db: Session = Depends(get_db)):
    return service.create_villain(db, villain)


@router.put("/villain/{villain_id}")
def update_villain(villain_id: int, villain: Villain, db: Session = Depends(get_db)):
    return service.update_villain(db, villain_id, villain)


@router.delete("/villain/{villain_id}")
def delete_villain(villain_id: int, db: Session = Depends(get_db)):
    return service.delete_villain(db, villain_id)


@router.post("/villain/{villain_id}/hero/{hero_id}", response_model=VillainWithHeroes)
def add_hero_to_villain(villain_id: int, hero_id: int, db: Session = Depends(get_db)):
    return service.add_hero_to_villain(db, villain_id, hero_id)


@router.delete("/villain/{villain_id}/hero/{hero_id}", response_model=VillainWithHeroes)
def remove_hero_from_villain(villain_id: int, hero_id: int, db: Session = Depends(get_db)):
    return service.remove_hero_from_villain(db, villain_id, hero_id)
