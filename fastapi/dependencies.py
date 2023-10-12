
from jose import JWTError, jwt

from jose.exceptions import JWTError

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param
from fastapi import Depends, HTTPException, Path, Query, Request
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
from models.models import Player

from jose import JWTError, jwt
from jose.exceptions import JWTError

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param
from fastapi import Depends, HTTPException, Path, Query, Request
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
from starlette.status import HTTP_404_NOT_FOUND
from starlette.status import *

import random
import math
from models.models import Player
auth_schema = HTTPBearer()
JWT_SECRET = "IamOmarAboelfetouhMahmoudAndIDoART01129461404"

async def jwt_required(
    request: Request, token: HTTPAuthorizationCredentials = Depends(auth_schema)
):
    credentials_exception = HTTPException(HTTP_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(token.credentials, JWT_SECRET)
        id = payload.get("id")
        if id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    request.scope["id"] = id
    return id


async def get_user(id=Depends(jwt_required)):
    user = await Player.findPlayerById(user_id=id)
    if not user:
        raise HTTPException(HTTP_404_NOT_FOUND)
    return user