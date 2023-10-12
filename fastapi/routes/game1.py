
import random
# import apply function and cach memory
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi import APIRouter, Depends
from fastapi import Path

from dependencies import auth_schema, JWT_SECRET, jwt_required, get_user
from models.schemas import GameOne, GameOneInput, GameOneOutput,GameId
from models.models import Player, LeaderBoardG1

'''
to use this just import
game_cache
generate_and_add_games_to_cache() # call this and make this awaited
'''

CashMem_sympoles = {
    1: '+',     # Sum
    2: '-',     # Subtract
    3: '*',     # Multiply
    4: '/'      # Divide
}

def calculate_answer(op1, op2, operation_id):
    if operation_id == 1:  # Addition
        return op1 + op2
    elif operation_id == 2:  # Subtraction
        return op1 - op2
    elif operation_id == 3:  # Multiplication
        return op1 * op2
    elif operation_id == 4:  # Division
        return op1 / op2

def generate_game(game_id):
    op1 = random.randint(0, 20)
    op2 = random.randint(1, 20)
    operation_id = random.randint(1, 3)
    
    game_data = {
        'FirstOperand': op1,
        'SecondOperand': op2,
        'OperationId': operation_id,
        'OperationSymbol': CashMem_sympoles[operation_id],
        'Answer': calculate_answer(op1, op2, operation_id)
    }
    return game_data

def generate_and_add_games_to_cache():
    game_cache = {}
    for i in range(10):
        game_id = i + 1  # Assuming game IDs start from 1
        game_cache[i] = generate_game(game_id)
    return game_cache
game_cache = generate_and_add_games_to_cache()
game_id = random.randint(0,9)
# instantiate the router for the Game 1 page :))

g1_router = APIRouter()

# you have to create the game_cache


# Assuming game is a global variable in your module
@g1_router.get('/game1')
async def display_game1(user=Depends(get_user)):
    '''
    This API is dedicated to display the question of game 1
    '''    
    # return equation, id equation
    game_id = random.randint(0,9)
    game = game_cache[game_id]
    equation = str(game['FirstOperand']) + " " + str(game['OperationSymbol']) + " " + str(game['SecondOperand'])
    return {'equation': equation, "game_id" : game_id}

@g1_router.post('/game1/{game_id}')
async def fitch_ans1( game_id: int , Ans: GameOneInput, user=Depends(get_user)):
    
    '''
    This API is dedicated to fetch the answer of game 1
    and recalculate the score - update it, it also may display it
    '''
    game = game_cache[game_id]
    gameout = {}
    
    if (Ans.Ans == game['Answer']):
        #calc the score
        gameout['score'] = 10 / Ans.time_taken
        gameout['status'] = True
        gameout['message'] = "Answer is correct"
    else:
        gameout['score'] = 0
        gameout['status'] = False
        gameout['message'] = "Answer is not correct"
    
    #update the database
    #updates the score and the total rank
    await user.update_score1(gameout['score'])
    
    new_leaderboard = await LeaderBoardG1.create(name=user.name, game1_score=gameout['score'], time_taken =  float(Ans.time_taken))
    # Save the instance
    await new_leaderboard.save()
    return {'message': gameout['message'], 'score' : gameout['score'] }


@g1_router.get('/leaderboard1')
async def leaderboard1(user=Depends(get_user)):
    '''
    this is to display the leaderboard of the fisrt game score bs
    '''
    leaders = await LeaderBoardG1.leaderboard()
    return {"leaderboard": leaders[:15]}


    