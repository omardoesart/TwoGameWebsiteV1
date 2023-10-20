'''
this file is dedicated to for the data classes that we need for the site
'''

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from passlib.hash import bcrypt
from fastapi import HTTPException, status
from passlib.context import CryptContext
from passlib.hash import bcrypt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Player(Model):
    id = fields.IntField(pk = True)
    
    # name is only used when you first get into the game
    # after that you only supposed to login with your username
    name = fields.CharField(50, unique = True)
    username = fields.CharField(50, unique = True)
    password = fields.CharField(200)

    game1_score = fields.IntField(default = 0)
    game2_score = fields.IntField(default = 0)
    total_score = fields.IntField(default = 0)

    is_blocked = fields.BooleanField(default = False)
    rank = fields.IntField(null = True)

    def get_password(self):
        return self.password
    
    @classmethod
    async def hash_password(cls, password):
        return pwd_context.hash(password)
    
    async def verify_password(self, provided_password):
        return pwd_context.verify(provided_password, self.password)

    @classmethod
    async def findPlayerById(cls, user_id):
        return await cls.filter(id = user_id).first()

    @classmethod
    async def findPlayerByUsername(cls, username):
        return await cls.filter(username = username).first()

    #V2 add the hash thing
    async def verify_password_login(self, x):
        if self.password == x:
            return True
        return False
        
    @classmethod
    async def verify_signup(cls,fieldsname ,data):
        '''
        this class method verifies that the username and name are not taken already
        it's only used when you sign up
        '''
        for f in fieldsname:
            if f == 'username':
                x = await cls.filter(username = data[f])
                if x is not None: 
                    raise HTTPException(status_code=400,
                    detail='this username is already taken')
            if f == 'name':
                x = await cls.filter(username = data[f])
                if x is not None: 
                    raise HTTPException(status_code=400,
                    detail='this Name is already taken')
    
    @classmethod
    async def verify_signin(cls,fieldsname ,data):
        '''
        this class method verifies the username
        it's only used when you login
        '''
        for f in fieldsname:
            if f == 'username':
                x = await cls.filter(username = data[f])
                if x is not None: 
                    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='this username is not a valid username, would you like to sign up?')
    
    async def update_score1(self, shot_score):
        '''
        this method updates the score for this game : game 1
        and the total score for the player : self
        '''
        self.game1_score += shot_score
        self.total_score += shot_score
        await self.save()
        ordered_data = await Player.all().order_by('total_score')
        for i, item in enumerate(ordered_data):
            item.rank = i + 1
            await item.save()

    async def update_score2(self, shot_score):
        '''
        this function updates the score for this game : game 2
        and the total score for the player : self
        '''
        self.game2_score += shot_score
        self.total_score += shot_score
        ordered_data = await Player.all().order_by('total_score')
        for i, item in enumerate(ordered_data):
            item.rank = i + 1
            await item.save()
                
    @classmethod
    async def leaderboard_game1(cls):
        ordered_data = await cls.all().order_by('-game1_score')
        return ordered_data

    @classmethod
    async def leaderboard_game2(cls):
        ordered_data = await cls.all().order_by('-game2_score')
        return ordered_data

    @classmethod 
    async def leaderboard(cls):
        ordered_data = await cls.all().order_by('-total_score')
        return ordered_data

class LeaderBoardG1(Model):
    name = fields.CharField(50)
    game1_score = fields.FloatField(default = 0)
    time_taken = fields.IntField(default=0.0)
    @classmethod
    async def leaderboard(cls):
        ordered_data = await cls.all().order_by('-game1_score')
        return cls._exclude_id_from_data(ordered_data)

    @staticmethod
    def _exclude_id_from_data(data):
        return [
            {key: value for key, value in item.__dict__.items() if key != 'id'}
            for item in data
        ]

    
class LeaderBoardG2(Model):
    name = fields.CharField(50)   
    game2_score = fields.FloatField(default = 0)
    @classmethod 
    async def leaderboard(cls):
        ordered_data = await cls.all().order_by('-game2_score')
        return cls._exclude_id_from_data(ordered_data)

    @staticmethod
    def _exclude_id_from_data(data):
        return [
            {key: value for key, value in item.__dict__.items() if key != 'id'}
            for item in data
        ]


