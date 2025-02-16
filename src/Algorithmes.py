import random
import time
from src.RushHour import RushHour
from src.Check import Check
from collections import deque
import heapq
import itertools


#Question 3: Implementation of the bruteforce algorithm using the implementation choice described in the report
def bfs(rush_hour_game, max_iterations=100000, debug=False, print_solution=True):
    """
    Breadth-First Search (BFS) to find the shortest solution for Rush Hour.
    """

    start_time = time.time()
    initial_state = rush_hour_game
    initial_key = str(initial_state.vehicles)  # Store as a string for fast comparison

    queue = deque()
    queue.append((initial_state, [initial_state]))  
    #to store the visited state to avoid replications
    visited = set()
    visited.add(initial_key)
    
    iterations = 0

    while queue:
        iterations += 1
        current_state, path = queue.popleft()

        # Optional debug: Print every 100 iterations
        if debug and iterations % 100 == 0:
            print(f"Iteration {iterations}: Queue size = {len(queue)}, Visited = {len(visited)}")

        # If winning state is found, reconstruct solution
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

        # to prevent overFlow error
        if iterations > max_iterations:
            elapsed_time = time.time() - start_time
            return {
                "message": "Max iterations reached. No solution found.",
                "iterations": iterations,
                "solvetime": elapsed_time
            }

        # Expand the current state by considering all possible moves.
        for move in current_state.get_possible_moves():
            new_state = RushHour(current_state.grid_size, list(move))
            new_key = str(new_state.vehicles)

            # Only add new states that have not been visited.
            if new_key not in visited:
                visited.add(new_key)
                new_path = path + [new_state]
                queue.append((new_state, new_path))
    #measured time execution
    elapsed_time = time.time() - start_time
    return {
        "message": "No solution found",
        "iterations": iterations,
        "solvetime": elapsed_time
    }

#Question 7: add some lines code from the bfs function to give the reconstruction path of the solution.
def reconstruct_path(predecessors, final_state):
    """
    Reconstructs the solution path from the winning state back to the initial state.
    - Traces back using the `predecessors` dictionary.
    - Returns the path in the correct order (initial → solution).
    """
    path = []
    current = final_state

    while current is not None:
        path.append(current)
        current = predecessors[str(current.vehicles)]  #Get the parent state
    # Reverse to get the correct order
    path.reverse()  
    return path

#In BFS, we don't have backtracking , since we explore all the states from the initial state. 
# In the case of DFS, one might use backtracking to find the solution 
def bfs_reconstruct_solution(rush_hour_game, max_iterations=100000, debug=False, print_solution=True):
    """
    Breadth-First Search (BFS) with backtracking for Rush Hour.
    - Uses a `predecessors` dictionary to store the parent state of each explored state.
    - Once a solution is found, backtracks to reconstruct the shortest path.
    """

    start_time = time.time()
    initial_state = rush_hour_game
    initial_key = str(initial_state.vehicles) #might take time to convert the vehicles to string (alternative way: use tuple(immutable list))

    queue = deque([initial_state])  # First in - First out
    visited = set([initial_key])    
    predecessors = {initial_key: None}  # Dictionary to track parent states

    iterations = 0

    while queue:
        iterations += 1
        current_state = queue.popleft()
        
        # Optional debug output
        if debug and iterations % 100 == 0:
            print(f"Iteration {iterations}: Queue size = {len(queue)}, Visited states = {len(visited)}")

        # If winning state is found, reconstruct path
        if current_state.check_winning():
            elapsed_time = time.time() - start_time
            solution_path = reconstruct_path(predecessors, current_state)
            
            if print_solution:
                print("\nSolution found!")
                print(f"Iterations: {iterations}")
                print(f"Execution time: {elapsed_time:.4f} seconds")
                print("\n--- Solution Path ---")
                for step, state in enumerate(solution_path):
                    print(f"\nStep {step}:")
                    state.display_grid()

            return {
                "solution": solution_path,
                "iterations": iterations,
                "solvetime": elapsed_time
            }
        #to prevent Overflow
        if iterations > max_iterations:
            elapsed_time = time.time() - start_time
            return {
                "message": "Max iterations reached. No solution found.",
                "iterations": iterations,
                "solvetime": elapsed_time
            }

        # BFS by considering all possible moves
        for move in current_state.get_possible_moves():
            new_state = RushHour(current_state.grid_size, list(move))
            new_key = str(new_state.vehicles)

            if new_key not in visited:
                visited.add(new_key)
                queue.append(new_state)
                predecessors[new_key] = current_state  
    #time of execution
    elapsed_time = time.time() - start_time
    return {
        "message": "No solution found",
        "iterations": iterations,
        "solvetime": elapsed_time
    }



#Question 8: the heuristic given by the subject using the number of vehicles between the red vehicle and the exit
def heuristic_nb_block(state):
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
 




#question 10

# Heuristic : The number of blocking vehicle between the red vechicle and the exit
def bfs_direct_blocking(initial_state, print_solution=True, max_iterations=100000):
    """
    BFS with heuristic using a number of blocking vehicles heuristic.
    - Uses a `predecessors` dictionary to store parent states for backtracking.
    - Uses a priority queue to expand nodes in order of `f = g + h`.
    - `g`: Number of moves taken so far.
    - `h`: Estimated cost (blocking heuristic).

    Parameters:
        initial_state (RushHour): The initial game state.
        print_solution (bool): Whether to print the solution path.
        max_iterations (int): Cutoff to prevent infinite loops.

    Returns:
        dict: Solution details including the solution path, iteration count, and execution time.
    """
    start_time = time.time()
    
    open_queue = []
    visited = {}
    predecessors = {}

    counter = itertools.count()  # Tie-breaker for queue stability

    initial_cost = 0 
    initial_h = heuristic_nb_block(initial_state)  # h-value (heuristic)
    initial_f = initial_cost + initial_h
    initial_state_repr = str(initial_state.vehicles)

    heapq.heappush(open_queue, (initial_f, initial_cost, next(counter), initial_state))
    visited[initial_state_repr] = initial_cost
    predecessors[initial_state_repr] = None

    iterations = 0

    while open_queue:
        iterations += 1
        elapsed_time = time.time() - start_time
        print(f"\nIteration {iterations} (Elapsed time: {elapsed_time:.2f} seconds) - Queue size: {len(open_queue)}")

        # Extract the best state from the priority queue
        f, cost, _, current_state = heapq.heappop(open_queue)
        current_state.display_grid()  
        
        #If winning is reached, print the results 
        if current_state.check_winning():
            elapsed_time = time.time() - start_time
            solution_path = reconstruct_path(predecessors, current_state)
            
            if print_solution:
                print("\nSolution found!")
                print(f"Iterations: {iterations}")
                print(f"Execution time: {elapsed_time:.4f} seconds")
                print("\n--- Solution Path ---")
                for step, state in enumerate(solution_path):
                    print(f"\nStep {step}:")
                    state.display_grid()

            return {
                "solution": solution_path,
                "iterations": iterations,
                "solvetime": elapsed_time
            }
        # prevent Overflow
        if iterations > max_iterations:
            elapsed_time = time.time() - start_time
            print(f"\nMax iterations ({max_iterations}) reached. No solution found.")
            return {
                "message": "Max iterations reached. No solution found.",
                "iterations": iterations,
                "solvetime": elapsed_time
            }
        # check for possible moves out of the current move to continue searching
        for move in current_state.get_possible_moves():
            new_state = RushHour(current_state.grid_size, list(move))
            new_state_repr = str(new_state.vehicles)
            new_cost = cost + 1  #Increment g-value

            old_g = visited.get(new_state_repr, float('inf'))
            if new_cost < old_g:
                visited[new_state_repr] = new_cost
                new_h = heuristic_nb_block(new_state)
                new_f = new_cost + new_h
                heapq.heappush(open_queue, (new_f, new_cost, next(counter), new_state))
                predecessors[new_state_repr] = current_state 

    print("No solution found.")
    return {
        "message": "No solution found",
        "iterations": iterations,
        "solvetime": elapsed_time
    }









### heuristic blockage penalty
#This function give the coordinate of the cell between the red car and the exit
def get_red_vehicle_path(state, red_vehicle):
    """
    Returns the list of positions that the red car needs to move to exit.
    """
    path = []
    red_vehicle_end = red_vehicle.x + red_vehicle.length
    for i in range(red_vehicle_end, state.grid_size + 1):  
        path.append((i, red_vehicle.y)) 
    return path

#This function give the vehicle that directly block the red car, the car must be verticle
def find_first_blocking_vehicle(state, red_vehicle_path):
    """
    Finds the first vehicle that directly blocks the red vehicle's path.
    """
    grid = state.build_grid()

    for x, y in red_vehicle_path: 
        # Check if the position is occupied by another vehicle 
        if grid[y - 1][x - 1] not in (".", "1"):  
            vehicle = state.get_vehicle_at(x, y)  
            if vehicle:
                return vehicle  

    return None  



#Find the positions that block the vehicle from above or below
def get_blocked_positions(state, vehicle, direction):
    """
    Returns the positions that the vertical car would occupy if it moves up/down,
    stopping once we find an occupied cell.
    """
    blocked_positions = []

    if direction == "UP":
        
        for row in range(vehicle.y - 1, 0, -1):
            if state.is_occupied((vehicle.x, row)):
                blocked_positions.append((vehicle.x, row))
                break  
    elif direction == "DOWN":
        
        for row in range(vehicle.y + vehicle.length, state.grid_size + 1):
            if state.is_occupied((vehicle.x, row)):
                blocked_positions.append((vehicle.x, row))
                break 

    return blocked_positions
# Find the vehicles that block the vehicle(parameter) form above or below. This function is the same as get_blocked_positions but different outputs.
def get_blockers(state, vehicle):
    """
    Returns a list (or set) of vehicles that block 'vehicle'
    from moving in each possible direction.
    """
    blockers = set()
    directions = ["UP", "DOWN"]  
    for direction in directions:
        blocked_positions = get_blocked_positions(state, vehicle, direction)
        for (x, y) in blocked_positions:
            occupant = state.get_vehicle_at(x, y)
            if occupant and occupant != vehicle:
                blockers.add(occupant)
    return blockers

# This function calculate the heuristic recursively taking into account the blocking constraint of the first car directly blocking the red car.
def chain_blockage_heuristic(state):
    """
    A multi-layered (chain) blockage heuristic:
    1) Find the first vehicle blocking the red car.
    2) If none, heuristic = 0.
    3) Otherwise, recursively penalize each chain of cars blocking the primary blocker.
    """
    
    red_car = next((v for v in state.vehicles if v.label == 1), None)
    if not red_car:
        return 0  

    red_car_path = get_red_vehicle_path(state, red_car)
    
    primary_blocker = find_first_blocking_vehicle(state, red_car_path)
    if not primary_blocker:
        return 0  

    # Penalize the chain of vehicles
    return 1 + chain_penalty(state, primary_blocker)


def chain_penalty(state, vehicle, visited=None):
    """
    Recursively calculates how many cars block this 'vehicle',
    plus how many cars block them, etc.
    """
    if visited is None:
        visited = set()
    if vehicle in visited:
        # Prevent infinite loops (e.g., if there's a circular block)
        return 0
    visited.add(vehicle)

    #  Find all blockers that prevent 'vehicle' from moving
    blockers = get_blockers(state, vehicle) 
    if not blockers:
       
        return 0

    
    # Add penalty for each blocker recursively
    penalty = 0
    for blk in blockers:
       
        penalty += 1 + chain_penalty(state, blk, visited)

    return penalty


#Question 11: our bfs algorithm using chain_blockage_heuristic
def bfs_with_blocking_penalty(rush_hour_game, print_solution=True, max_iterations=100000):
    """
    - Priority queue items: (f, g, tie_breaker, current_state, path)
    - 'visited_states' keeps track of the best g so far for each state.
    - 'visited_edges' ensures we don't re-traverse the same (old_state -> new_state).

    Returns:
       dict with {"solution": [...], "iterations": <int>, "solvetime": <float>}
       or "NO_SOLUTION_FOUND" if no path is found.
    """
    start_time = time.time()

    open_queue = []
    visited_states = {}  
    visited_edges = set()  
    counter = itertools.count()

    # Initial cost
    initial_g = 0
    initial_h = chain_blockage_heuristic(rush_hour_game)
    initial_f = initial_g + initial_h
    init_repr = str(rush_hour_game.vehicles)

 
    heapq.heappush(open_queue, (initial_f, initial_g, next(counter), rush_hour_game, [rush_hour_game]))
    visited_states[init_repr] = initial_g

    iterations = 0
    while open_queue:
        iterations += 1

        
        if iterations > max_iterations:
            elapsed_time = time.time() - start_time
            print(f"Max iterations ({max_iterations}) reached. Execution time={elapsed_time:.4f}s")
            return {
                "message": "Max iterations reached. No solution found.",
                "iterations": iterations,
                "solvetime": elapsed_time
            }

        f, g, _, current_state, path = heapq.heappop(open_queue)
        current_repr = str(current_state.vehicles)

        # Print solution parametre if winning exists
        if current_state.check_winning():
            elapsed_time = time.time() - start_time
            if print_solution:
                print(f"\nSolution found in {iterations} iterations, time={elapsed_time:.2f}s")
                print("\n--- Solution Path ---")
                for step_idx, st in enumerate(path):
                    print(f"\nStep {step_idx}:")
                    st.display_grid()
            return {
                "solution": path,
                "iterations": iterations,
                "solvetime": elapsed_time
            }

    
        possible_moves = current_state.get_possible_moves()

        for move in possible_moves:
            new_state = RushHour(current_state.grid_size, list(move))
            new_state_repr = str(new_state.vehicles)
            new_g = g + 1

            # create edge connecting new vertex with previous vertex
            edge = (current_repr, new_state_repr)

            if edge in visited_edges:
                continue
            visited_edges.add(edge)

            old_g = visited_states.get(new_state_repr, float("inf"))
            if new_g < old_g:
                
                visited_states[new_state_repr] = new_g
                new_h = chain_blockage_heuristic(new_state)
                new_f = new_g + new_h
                new_path = path + [new_state]
                heapq.heappush(open_queue, (new_f, new_g, next(counter), new_state, new_path))
    #Print time of execution          
    elapsed_time = time.time() - start_time
    print(f"No solution found. Execution time={elapsed_time:.4f}s")
    return "NO_SOLUTION_FOUND"