from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi import APIRouter, Depends

# instantiate the router for the Game 1 page :))
router = APIRouter()

@router.get('\leaderboard')
async def leaderboard():
    '''
    show all players score for both games 
    order them based on the sum of the two score
    '''
    pass

@router.get('\leaderboard\game1')
async def leaderboard_game1():
    '''
    show all players score for first game2 
    order them based on the sum of the first score
    '''
    pass

@router.get('\leaderboard\game2')
async def leaderboard_game2():
    '''
    show all players score for second game2
    order them based on the sum of the second score
    '''
    pass