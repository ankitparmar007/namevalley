from fastapi import FastAPI
from typing import Optional

# from pydantic import BaseModel
# images/pink/?skip=0&limit=5

app = FastAPI()

# @app.get("/images/blue/")
# async def blue_image(skip: int = 0, limit: int = 10):
#     return blue_image_db[skip: skip + limit]

@app.get("/")
async def root():
    return main_image_db

main_image_db = [
#     {"image_url": "/images/blue/"},
    {"image_url": "/images/pink/"},
    {"image_url": "/images/pastel_green/"},
    {"image_url": "/images/red/"},
    {"image_url": "/images/green/"},
    {"image_url": "/images/cyan/"},
]

blue_image_db = {
    "imagesList" : [
    {"image_url": "https://i.ibb.co/f4P136b/blueback.jpg"},
    {"image_url": "https://i.ibb.co/tJDQNxX/6-blue-doll.png"},
    {"image_url": "https://i.ibb.co/GPrXvyG/5-blue-lemon.png"},
    {"image_url": "https://i.ibb.co/K24YvqL/4-blue-donot.png"},
    {"image_url": "https://i.ibb.co/xg02PQz/13-blue-lemon.png"},
    {"image_url": "https://i.ibb.co/CHVckVV/14-blue-pineapple.png"},
    {"image_url": "https://i.ibb.co/4F6QNF6/15-blue-pineapple2.png"},
]
}

pink_image_db = {
    "imagesList":[
    {"image_url": "https://i.ibb.co/zGKjp7t/7-pink-pineapple.png"},
    {"image_url": "https://i.ibb.co/RQSjMvb/8-pink-doll.png"},
    {"image_url": "https://i.ibb.co/YbbS5vW/9-pink-pineapple.png"},
    {"image_url": "https://i.ibb.co/Jm8f1jV/16-pink-lemon.png"},
    {"image_url": "https://i.ibb.co/Gn1qcKg/17-pink-lemon2.png"},
    {"image_url": "https://i.ibb.co/h8vMNwc/18-pink-pineapple.png"},
]
}

pastel_green_image_db = {
    "imagesList":[
    {"image_url": "https://i.ibb.co/MGSCxX7/1-pastel-donote.png"},
    {"image_url": "https://i.ibb.co/pbCd1X2/2-Pastel-melon.png"},
    {"image_url": "https://i.ibb.co/2yQ1r30/3-Pastel-banana.png"},
    {"image_url": "https://i.ibb.co/92g8MHb/10-pgreen-orange.png"},
    {"image_url": "https://i.ibb.co/CzhQ29N/11-pgreen-pineapple.png"},
    {"image_url": "https://i.ibb.co/6HkdLZq/12-pgreen-melon.png"},
]
}





red_image_db = {
    "imagesList":[
    {"image_url": "https://i.ibb.co/3Y2vwQX/7-red-glass.png"},
    {"image_url": "https://i.ibb.co/yRMDzGm/8-red-flower.png"},
    {"image_url": "https://i.ibb.co/RCnnjVh/9-red-ice-cream.png"},
]
}





green_image_db = {
    "imagesList":[
    {"image_url": "https://i.ibb.co/ZWHQXQv/1-green-coco.png"},
    {"image_url": "https://i.ibb.co/ZXrzPRF/2-green-pineapple.png"},
    {"image_url": "https://i.ibb.co/5kjQMr8/3-green-pineapple2.png"},
]
}





cyan_image_db = {
    "imagesList":[
    {"image_url": "https://i.ibb.co/NmsrPQ5/4-cyan-flower.png"},
    {"image_url": "https://i.ibb.co/7jCdm3F/5-cyan-watermelon.png"},
    {"image_url": "https://i.ibb.co/X4DzV6b/6-cyan-coco.png"},
]
}

test_image_db = [
    {"image_url": "https://i.ibb.co/f4P136b/blueback.jpg"},
    {"image_url": "https://i.ibb.co/tJDQNxX/6-blue-doll.png"},
    {"image_url": "https://i.ibb.co/GPrXvyG/5-blue-lemon.png"},
    {"image_url": "https://i.ibb.co/K24YvqL/4-blue-donot.png"},
    {"image_url": "https://i.ibb.co/xg02PQz/13-blue-lemon.png"},
    {"image_url": "https://i.ibb.co/CHVckVV/14-blue-pineapple.png"},
    {"image_url": "https://i.ibb.co/4F6QNF6/15-blue-pineapple2.png"},
    {"image_url": "https://i.ibb.co/zGKjp7t/7-pink-pineapple.png"},
    {"image_url": "https://i.ibb.co/RQSjMvb/8-pink-doll.png"},
    {"image_url": "https://i.ibb.co/YbbS5vW/9-pink-pineapple.png"},
    {"image_url": "https://i.ibb.co/Jm8f1jV/16-pink-lemon.png"},
    {"image_url": "https://i.ibb.co/Gn1qcKg/17-pink-lemon2.png"},
    {"image_url": "https://i.ibb.co/h8vMNwc/18-pink-pineapple.png"},
    {"image_url": "https://i.ibb.co/MGSCxX7/1-pastel-donote.png"},
    {"image_url": "https://i.ibb.co/pbCd1X2/2-Pastel-melon.png"},
    {"image_url": "https://i.ibb.co/2yQ1r30/3-Pastel-banana.png"},
    {"image_url": "https://i.ibb.co/92g8MHb/10-pgreen-orange.png"},
    {"image_url": "https://i.ibb.co/CzhQ29N/11-pgreen-pineapple.png"},
    {"image_url": "https://i.ibb.co/6HkdLZq/12-pgreen-melon.png"},
    {"image_url": "https://i.ibb.co/NmsrPQ5/4-cyan-flower.png"},
    {"image_url": "https://i.ibb.co/7jCdm3F/5-cyan-watermelon.png"},
    {"image_url": "https://i.ibb.co/X4DzV6b/6-cyan-coco.png"},
    {"image_url": "https://i.ibb.co/3Y2vwQX/7-red-glass.png"},
    {"image_url": "https://i.ibb.co/yRMDzGm/8-red-flower.png"},
    {"image_url": "https://i.ibb.co/RCnnjVh/9-red-ice-cream.png"},
    {"image_url": "https://i.ibb.co/ZWHQXQv/1-green-coco.png"},
    {"image_url": "https://i.ibb.co/ZXrzPRF/2-green-pineapple.png"},
    {"image_url": "https://i.ibb.co/5kjQMr8/3-green-pineapple2.png"},
]

@app.get("/images/blue/")
async def blue_image():
    return blue_image_db


@app.get("/images/pastel_green/")
async def pastel_green_image():
    return pastel_green_image_db

@app.get("/images/pink/")
async def pink_image():
    return pink_image_db

@app.get("/images/red/")
async def red_image():
    return red_image_db

@app.get("/images/green/")
async def green_image():
    return green_image_db

@app.get("/images/cyan/")
async def cyan_image():
    return cyan_image_db

@app.get("/images/test/")
async def test_image():
    return test_image_db
