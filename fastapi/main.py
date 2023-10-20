from fastapi import Depends, FastAPI
from routes.home import h_router
from routes.game1 import g1_router
from routes.game2 import g2_router

from jose import JWTError, jwt
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt

from tortoise import Tortoise
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from passlib.hash import bcrypt

from passlib.hash import bcrypt
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(h_router)
app.include_router(g1_router)
app.include_router(g2_router)

@app.get("/")
async def read_root():
    return {"Hello": "hiii"}

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',  
    modules={'models': ['models.models']},  
    generate_schemas=True,
    add_exception_handlers=True
)