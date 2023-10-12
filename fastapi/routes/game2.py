from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi import APIRouter, Depends

# instantiate the router for the Game 1 page :))
router = APIRouter()

@router.get('\game2')
async def display_game2():
    '''
    this api is dedicated to display the question of game 2
    '''
    pass

@router.post('\game2')
async def fitch_ans2():
    '''
    this api is dedicated to fitch the answer of game 2
    and recalculate the score - update it, it also may display it
    '''
    pass

@router.get('/game2/leaderboard2')
async def leaderboard2():
    '''
    this is to display the leaderboard of the second game score bs
    '''
    leaders = await Player.leaderboard_game2()
    return {"leader board": leaders}