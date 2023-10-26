from fastapi import Body
from pydantic import BaseModel, Field

class RegistrationPydantic(BaseModel):
    username: str = Body(..., example="omardoesart")
    password: str = Body(..., example = "My Password")
    name: str = Body(..., example = "Omar Aboelfetouh")

class LoginPydantic(BaseModel):
    username: str = Body(..., example="OmarAboelfetouh204")
    password: str = Body(..., example = "My Password")

class RankMapOut(BaseModel):
    Name : str
    Rank : int

    
class GameOne(BaseModel):
    FirstOprand : float
    SecondOprand : float
    #oprand is the key in the cach memory, its value is a poGameOneInputer to the right function
    Operation_id: int
    Operation_sympol : str
    ans : float

class GameOneInput(BaseModel):
    Ans : int
    time_taken : int
    ansRecieved : int

class GameOneOutput(BaseModel):
    '''
    status : true or false
    score : if true, you get a score based on the time you spend answering this question
    '''
    status: bool
    score : int
    message : str


class GameTwoInput(BaseModel):
    points : int
    

    
class User_PY(BaseModel):
    name : str


    
class GameId(BaseModel):
    id : int

