from fastapi import FastAPI,HTTPException
from schemas import Hero

# creo mi instancia de FastAPI

app = FastAPI()

# armemos nuestra "db"

data = [
    {
        "name": "Hulk",
        "age": 50,
        "city": "New York"
    },
    {
        "name": "Thor",
        "age": 1500,
        "city": "Asgard"
    },
    {
        "name": "Spiderman",
        "age": 30,
        "city": "New York"
    }
]

# armemos los "endpoints"

@app.get("/hero")
def get_heroes():
    return data

@app.get("/hero/{hero_id}")
def get_hero(hero_id: int):
    if not hero_id in range(len(data)):
        raise HTTPException(status_code=404, detail="Hero not found")
    return data[hero_id]

@app.post("/hero")
def create_hero(hero: Hero):
    data.append(hero.model_dump())
    return data[-1]

@app.put("/hero/{hero_id}")
def update_hero(hero_id: int, hero: Hero):
    if not hero_id in range(len(data)):
        raise HTTPException(status_code=404, detail="Hero not found")
    data[hero_id] = hero.model_dump()
    return data[hero_id]


@app.delete("/hero/{hero_id}")
def delete_hero(hero_id: int):
    if not hero_id in range(len(data)):
        raise HTTPException(status_code=404, detail="Hero not found")
    data.pop(hero_id)
    return data
