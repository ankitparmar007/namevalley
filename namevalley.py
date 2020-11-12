from fastapi import FastAPI
from typing import Optional

# from pydantic import BaseModel
# images/pink/?skip=0&limit=5

app = FastAPI()


@app.get("/")
async def root(skip: int = 0, limit: int = 10):
    return main_image_db[skip: skip + limit]

main_image_db = [
    {"image_url": "/images/blue/?skip=0&limit=5"},
    {"image_url": "/images/pink/?skip=0&limit=5"},
    {"image_url": "/images/pastel_green/?skip=0&limit=5"},
]

blue_image_db = [
    {"image_url": "https://i.ibb.co/f4P136b/blueback.jpg"},
    {"image_url": "https://i.ibb.co/tJDQNxX/6-blue-doll.png"},
    {"image_url": "https://i.ibb.co/GPrXvyG/5-blue-lemon.png"},
    {"image_url": "https://i.ibb.co/K24YvqL/4-blue-donot.png"},
]

pink_image_db = [
    {"image_url": "https://i.ibb.co/zGKjp7t/7-pink-pineapple.png"},
    {"image_url": "https://i.ibb.co/RQSjMvb/8-pink-doll.png"},
    {"image_url": "https://i.ibb.co/YbbS5vW/9-pink-pineapple.png"},
]

pastel_green_image_db = [
    {"image_url": "https://i.ibb.co/MGSCxX7/1-pastel-donote.png"},
    {"image_url": "https://i.ibb.co/pbCd1X2/2-Pastel-melon.png"},
    {"image_url": "https://i.ibb.co/2yQ1r30/3-Pastel-banana.png"},
]


@app.get("/images/blue/")
async def blue_image(skip: int = 0, limit: int = 10):
    return blue_image_db[skip: skip + limit]


@app.get("/images/pastel_green/")
async def pastel_green_image(skip: int = 0, limit: int = 10):
    return pastel_green_image_db[skip: skip + limit]

@app.get("/images/pink/")
async def pink_image(skip: int = 0, limit: int = 10):
    return pink_image_db[skip: skip + limit]



