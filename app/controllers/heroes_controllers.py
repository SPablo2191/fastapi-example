from fastapi import APIRouter
from app.services import HeroesService
from app.schemas import Hero

router  = APIRouter(prefix="/heroes", tags=["Heroes"])
service = HeroesService()

@router.get("/hero")
def get_heroes():
    return service.get_heroes()

@router.get("/hero/{hero_id}")
def get_hero(hero_id: int):
    return service.get_hero(hero_id)

@router.post("/hero")
def create_hero(hero: Hero):
    return service.create_hero(hero)

@router.put("/hero/{hero_id}")
def update_hero(hero_id: int, hero: Hero):
    return service.update_hero(hero_id, hero)


@router.delete("/hero/{hero_id}")
def delete_hero(hero_id: int):
    return service.delete_hero(hero_id)
