from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi import APIRouter, Depends
from models.schemas import GameTwoInput
from models.models import Player, LeaderBoardG2
from dependencies import get_user

# instantiate the router for the Game 1 page :))
g2_router = APIRouter()

@g2_router.post('/game2')
async def fitch_ans2(ans : GameTwoInput, user=Depends(get_user)):
    '''
    this api is dedicated to fitch the answer of game 2
    and recalculate the score - update it, it also may display it
    '''
    await user.update_score2(gameout['score'])
    await user.update_score2(ans.points)
    new_leaderboard = await LeaderBoardG2.create(name=user.name, game2_score=ans.points)
    await new_leaderboard.save()
    
    return {'message':'points saved!'}

@g2_router.get('/leaderboard2')
async def leaderboard1(user=Depends(get_user)):
    '''
    this is to display the leaderboard of the fisrt game score bs
    '''
    leaders = await LeaderBoardG2.leaderboard()
    return {"leaderboard": leaders[:15]}
