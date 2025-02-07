import random
import time
from src.RushHour import RushHour
from collections import deque


def brute_force(rush_hour_game, max_iterations=100000):
    """
    Performs a random walk (brute force) to try to solve the RushHour game.
    Note: This is not a systematic search and may not find a solution.
    
    Parameters:
        rush_hour_game (RushHour): The initial game state.
        max_iterations (int): Maximum number of iterations to attempt.
    
    Returns:
        dict
    """
    start_time = time.time()
    current_state = rush_hour_game
    explored_states = set()
    path = [current_state]
    iterations = 0

    while iterations < max_iterations:
        iterations += 1
        state_key = tuple(current_state.vehicles)
        if state_key in explored_states:
           
            break
        explored_states.add(state_key)

        if current_state.check_winning():
            return {
                "solution": path,
                "solvetime": time.time() - start_time,
                "iterations": iterations
            }

        possible_moves = current_state.check_possible_move()
        if not possible_moves:
            break

       
        move = random.choice(list(possible_moves))
        new_state = RushHour(current_state.grid_size, list(move))
        path.append(new_state)
        current_state = new_state

    return {
        "message": "No solution found",
        "iterations": iterations,
        "solvetime": time.time() - start_time
    }




def dfs(rush_hour_game, max_iterations=100000, debug=False, print_solution=True):
    """
    Performs a Depth-First Search (DFS) to solve the RushHour game.
    """
    start_time = time.time()
    initial_key = tuple(rush_hour_game.vehicles)

    stack = [rush_hour_game]

    predecessors = {initial_key: None}
   
    state_instances = {initial_key: rush_hour_game}
    
    iterations = 0

    while stack:
        current_state = stack.pop()
        iterations += 1
        current_key = tuple(current_state.vehicles)

        if debug:
            print(f"Iteration {iterations}: Stack size = {len(stack)}, Visited states = {len(predecessors)}")

        if current_state.check_winning():
         
            solution_path = []
            key = current_key
            while key is not None:
                solution_path.append(state_instances[key])
                key = predecessors[key]
            solution_path.reverse()
            elapsed_time = time.time() - start_time
            print(f"\nSolution found in {iterations} iterations, execution time: {elapsed_time:.4f} seconds")
            
            if print_solution:
                print("\n--- Solution Path ---")
                for step, state in enumerate(solution_path):
                    print(f"\nStep {step}:")
                    state.display_grid()
            
            return {
                "solution": solution_path,
                "iterations": iterations,
                "solvetime": elapsed_time
            }

        if iterations > max_iterations:
            elapsed_time = time.time() - start_time
            print(f"Max iterations reached ({iterations}). Execution time: {elapsed_time:.4f} seconds")
            return {
                "message": "Max iterations reached. No solution found.",
                "iterations": iterations,
                "solvetime": elapsed_time
            }

   
        for move in current_state.get_possible_moves():
            new_state = RushHour(current_state.grid_size, list(move))
            new_key = tuple(new_state.vehicles)
            if new_key not in predecessors:
                predecessors[new_key] = current_key  
                state_instances[new_key] = new_state
                stack.append(new_state)

    elapsed_time = time.time() - start_time
    print(f"No solution found. Execution time: {elapsed_time:.4f} seconds")
    return {
        "message": "No solution found",
        "iterations": iterations,
        "solvetime": elapsed_time
    }
