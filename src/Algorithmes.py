import random
import time
from src.RushHour import RushHour
from collections import deque
import heapq
import itertools
#random walk
def brute_force(rush_hour_game, max_iterations=100000):
   
    start_time = time.time()
    current_state = rush_hour_game
    
    explored_states = set()
    # holds the sequence of states visited so we can backtrack.
    path = [current_state]
    iterations = 0

    while iterations < max_iterations:
        iterations += 1

        if current_state.check_winning():
            return {
                "solution": path,
                "solvetime": time.time() - start_time,
                "iterations": iterations
            }
        
        possible_moves = current_state.get_possible_moves()
        movable = []
        for move in possible_moves:
            move_key = tuple(move)
            if move_key not in explored_states:
                movable.append(move)    
                
                        
        if not movable:
            if len(path)>1:
                path.pop()
                current_state = path[-1]  
                continue
            else:
                break  
        
        move = random.choice(movable) 
        new_state = RushHour(current_state.grid_size, list(move))
        
        explored_states.add(tuple(new_state.vehicles))
     
    
        print(f"\nIteration {iterations}: New state chosen")
        new_state.display_grid()
        
        path.append(new_state)
        current_state = new_state

    return {
        "message": "No solution found",
        "iterations": iterations,
        "solvetime": time.time() - start_time
    }



#Question 3: Describe the brute-force algorithm and write its pseudocode
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
    
    
def bfs(rush_hour_game, max_iterations=100000, debug=False, print_solution=True):
  
    start_time = time.time()
    

    initial_state = rush_hour_game
    initial_key = tuple(initial_state.vehicles)
    
  
    queue = deque()
    queue.append((initial_state, [initial_state]))

    visited = set()
    visited.add(initial_key)
    
    iterations = 0

    while queue:
        iterations += 1
        current_state, path = queue.popleft()
        current_key = tuple(current_state.vehicles)
        
        if debug:
            print(f"Iteration {iterations}: Queue size = {len(queue)}, Visited states = {len(visited)}")

        if current_state.check_winning():
            elapsed_time = time.time() - start_time
            if print_solution:
                print("\nSolution found!")
                print(f"Iterations: {iterations}")
                print(f"Execution time: {elapsed_time:.4f} seconds")
                print("\n--- Solution Path ---")
                for step, state in enumerate(path):
                    print(f"\nStep {step}:")
                    state.display_grid()
            return {
                "solution": path,
                "iterations": iterations,
                "solvetime": elapsed_time
            }
        
        if iterations > max_iterations:
            break
        
        # Expand the current state by considering all possible moves.
        for move in current_state.get_possible_moves():
            # Create the new state by applying the move.
            new_state = RushHour(current_state.grid_size, list(move))
            new_key = tuple(new_state.vehicles)
            
            # Only add new states that have not been visited.
            if new_key not in visited:
                visited.add(new_key)
                new_path = path + [new_state]
                queue.append((new_state, new_path))
    
    elapsed_time = time.time() - start_time
    return {
        "message": "No solution found",
        "iterations": iterations,
        "solvetime": elapsed_time
    }





def heuristic(state):
    """
    A heuristic function that estimates how far the state is from the solution.
    It returns the number of distinct vehicles that block the red car (vehicle with label 1)
    from exiting to the right. Assumes:
      - The red car has label 1 and is horizontal.
      - The red car exits from the right side of the grid.
    """
    red_car = None
    
    for vehicle in state.vehicles:
        if vehicle.label == 1:
            red_car = vehicle
            break
    if red_car is None:
        return float('inf')
    
    red_right = red_car.x + red_car.length - 1  
    red_row = red_car.y  
    

    grid = state.build_grid()
    

    blocking = set()
   
    for col in range(red_right, state.grid_size):
        cell = grid[red_row - 1][col]  # grid is 0-indexed
      
        if cell != "." and cell != "1":
            blocking.add(cell)
    
    return len(blocking)





def BFS_search_with_heuristic_approach(initial_state):
    """
 
    At each iteration, it prints the iteration count, elapsed time, queue size, and
    displays the current state's grid.
    
    Parameters:
        initial_state (RushHour): The initial RushHour state.
        
    Returns:
        A list representing the path (sequence of RushHour states) from the initial state
        to a winning state (where check_winning() is True). If no solution is found,
        returns "NO_SOLUTION_FOUND".
    """
    start_time = time.time()
    
    Q = []
  
    visited = {}
    
    counter = itertools.count()
    
    initial_g = 0
    initial_h = heuristic(initial_state)
    initial_f = initial_g + initial_h
    initial_state_repr = str(initial_state.vehicles)
    
    heapq.heappush(Q, (initial_f, initial_g, next(counter), initial_state, [initial_state]))
    visited[initial_state_repr] = initial_g

    iteration = 0
    while Q:
        iteration += 1
        elapsed_time = time.time() - start_time
        print(f"\nIteration {iteration} (Elapsed time: {elapsed_time:.2f} seconds) - Queue size: {len(Q)}")
        
     
        f, g, _, current_state, path = heapq.heappop(Q)
        
        
        current_state.display_grid()
        
      
        if current_state.check_winning():
            print(f"\n Solution found after {iteration} iterations and {elapsed_time:.2f} seconds!")
            return path
        
  
        for move in current_state.get_possible_moves():
            new_state = RushHour(current_state.grid_size, list(move))
            new_state_repr = str(new_state.vehicles)
            new_g = g + 1  
            
          
            if new_state_repr not in visited or new_g < visited[new_state_repr]:
                visited[new_state_repr] = new_g
                new_h = heuristic(new_state)
                new_f = new_g + new_h
                new_path = path + [new_state]
                heapq.heappush(Q, (new_f, new_g, next(counter), new_state, new_path))
    
    print(" No solution found.")
    return "NO_SOLUTION_FOUND"
