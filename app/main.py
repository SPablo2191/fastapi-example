from fastapi import FastAPI
from app.controllers import heroes_router
from app.repositories.database import Base,engine
# creo mi instancia de FastAPI

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(router=heroes_router, prefix=f"/api/v1")
