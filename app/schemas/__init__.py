from pydantic import BaseModel


class Hero(BaseModel):
    name: str
    age: int
    city: str