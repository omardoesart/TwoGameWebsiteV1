import random
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





# Assuming you have the previous code with generate_game_cache() function

