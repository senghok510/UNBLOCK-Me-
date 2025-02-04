
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

