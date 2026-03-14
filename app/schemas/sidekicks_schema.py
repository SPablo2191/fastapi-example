from pydantic import BaseModel


class Sidekick(BaseModel):
    hero_id: int
    name: str
    superpower: str
