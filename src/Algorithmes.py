
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
    explored_states = set()  # To track explored game states

    while True:
        # Get possible moves from the current game state
        possible_moves = possible_states  # This is now a set of frozensets
        
        if not possible_moves:
            break  

        # Pick a random move from the possible moves
        random_move = random.choice(list(possible_moves))  # Convert to list to pick a random move

        # Check if we've already explored this state
        if random_move in explored_states:
            continue  # Skip this move if it's already explored

        # Mark the state as explored
        explored_states.add(random_move)

        # Create a new game instance with the chosen move
        new_game = RushHour(current_game.grid_size, list(random_move))  # Convert frozenset back to list for the game
        steps += 1

        # Check if the new game state is a winning state
        if new_game.check_winning():
            return {"solvetime": time.time() - start_time, "steps": steps}
    
    return {"solvetime": time.time() - start_time, "steps": steps, "message": "No solution found"}

