from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services import SidekicksService
from app.schemas import Sidekick

router = APIRouter(prefix="/sidekicks", tags=["Sidekicks"])
service = SidekicksService()


@router.get("/sidekick")
def get_sidekicks(db: Session = Depends(get_db)):
    return service.get_sidekicks(db)


@router.get("/sidekick/{sidekick_id}")
def get_sidekick(sidekick_id: int, db: Session = Depends(get_db)):
    return service.get_sidekick(db, sidekick_id)


@router.get("/hero/{hero_id}")
def get_sidekicks_by_hero(hero_id: int, db: Session = Depends(get_db)):
    return service.get_sidekicks_by_hero(db, hero_id)


@router.post("/sidekick")
def create_sidekick(sidekick: Sidekick, db: Session = Depends(get_db)):
    return service.create_sidekick(db, sidekick)


@router.put("/sidekick/{sidekick_id}")
def update_sidekick(sidekick_id: int, sidekick: Sidekick, db: Session = Depends(get_db)):
    return service.update_sidekick(db, sidekick_id, sidekick)


@router.delete("/sidekick/{sidekick_id}")
def delete_sidekick(sidekick_id: int, db: Session = Depends(get_db)):
    return service.delete_sidekick(db, sidekick_id)
