from fastapi import FastAPI
from app.controllers import heroes_router, sidekicks_router, villains_router
from fastapi.middleware.cors import CORSMiddleware
from app.repositories.database import Base,engine
# creo mi instancia de FastAPI

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=heroes_router, prefix=f"/api/v1")
app.include_router(router=sidekicks_router, prefix=f"/api/v1")
app.include_router(router=villains_router, prefix=f"/api/v1")
