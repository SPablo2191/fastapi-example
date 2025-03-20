from fastapi import FastAPI
from app.controllers import heroes_router

# creo mi instancia de FastAPI

app = FastAPI()

app.include_router(router=heroes_router, prefix=f"/api/v1")
