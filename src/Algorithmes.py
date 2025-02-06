
import random
import time
from src.RushHour import RushHour
import time
import random
# Question 3

def Brute_Force(rush_hour_game, possible_states):
    start_time = time.time()
    current_game = rush_hour_game
    steps = 0
    explored_states = set()  

    while True:

        possible_moves = possible_states  
        
        if not possible_moves:
            break  

    
        random_move = random.choice(list(possible_moves))  # Convert to list to pick a random move

        if random_move in explored_states:
            continue 

 
        explored_states.add(random_move)

    
        new_game = RushHour(current_game.grid_size, list(random_move))  # Convert frozenset back to list for the game
        steps += 1

        if new_game.check_winning():
            return {"solvetime": time.time() - start_time, "steps": steps}
    
    return {"solvetime": time.time() - start_time, "steps": steps, "message": "No solution found"}


def DFS(rush_hour_game):
    
    Stack = []
    memo = {}
    memo[rush_hour_game] = 0
    #visited 
    Stack.append(rush_hour_game)
    count = 0
    while len(Stack) != 0:
        count += 1
        state = Stack.pop()
        
        if state.check_winning():
            print("Has solution")
        
        else:
            for possible_move in state.check_possible_move():
                new_state = RushHour(state.grid_size,possible_move)
                if new_state in memo:
                    pass
                else:
                    memo[new_state] = state
                    Stack.append(new_state)
        
    return False

def DFS(rush_hour_game):

    Stack = []
    visited = []
    step = 0 #steps to get to the solution
    Stack.append(rush_hour_game)
    while len(Stack) != 0:
        step += 1
        state = Stack.pop()
        if state in visited:
            pass
        visited.append(state)
        for possible in state.check_possible_move():
            new_state = RushHour(state.grid_size, possible)
    