from datetime import datetime
import uuid
from jose import JWTError, jwt
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query, APIRouter, Request
from fastapi.security import OAuth2PasswordBearer

from dependencies import auth_schema, JWT_SECRET, jwt_required, get_user
from models.schemas import LoginPydantic, RegistrationPydantic, User_PY
from models.models import Player



from passlib.context import CryptContext
from passlib.hash import bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
JWT_SECRET = "IamOmarAboelfetouhMahmoudAndIDoART01129461404"

# instantiate the router for the home page :))
h_router = APIRouter()
@h_router.post('/login')
async def login(login_pydantic: LoginPydantic):
    model = Player
    try:
        reg_dict = login_pydantic.dict(exclude_unset=True)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You are missing some information!')
    
    user = await model.findPlayerByUsername(reg_dict["username"])
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Username is not signed up!')
    
    
    # V2 add the hash thing
    v = pwd_context.verify(reg_dict["password"], user.get_password())
    if not v:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Password is not correct!')
    
    
    # the token generation
    token = jwt.encode({"id": user.id}, JWT_SECRET, algorithm="HS256")
    ret = {
        "user": {
            "username": user.username,
            "name": user.name,
        },
        "token": token
    }
    return {"access_token": token, "token_type": "bearer"}


@h_router.post('/register')
async def register(reg_pydantic : RegistrationPydantic):
    model = Player
    try:
           reg_dict = reg_pydantic.dict(exclude_unset = False)
    except:
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='You missing some information!')
    
    # save in database
    reg_dict['password'] = pwd_context.hash(reg_dict['password'])
    user = await model.create(**reg_dict)
    return user
    await user.save()

    # the token generation
    token = jwt.encode({"id": user.id}, JWT_SECRET, algorithm="HS256")
    ret = {
        "user": {
            "username": user.username,
            "avatar": user.picture if user.hasPicture() else None,
        },
        "token": token
    }
    return {"access_token": token, "token_type": "bearer"}

