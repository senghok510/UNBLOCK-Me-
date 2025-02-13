import random
import time
from src.RushHour import RushHour
from src.Check import Check
from collections import deque
import heapq
import itertools
# #random walk
# def random(rush_hour_game, max_iterations=100000):
   
#     start_time = time.time()
#     current_state = rush_hour_game
    
#     explored_states = set()
#     # holds the sequence of states visited so we can backtrack.
#     path = [current_state]
#     iterations = 0

#     while iterations < max_iterations:
#         iterations += 1

#         if current_state.check_winning():
#             return {
#                 "solution": path,
#                 "solvetime": time.time() - start_time,
#                 "iterations": iterations
#             }
        
#         possible_moves = current_state.get_possible_moves()
#         movable = []
#         for move in possible_moves:
#             move_key = tuple(move)
#             if move_key not in explored_states:
#                 movable.append(move)    
                
                        
#         if not movable:
#             if len(path)>1:
#                 path.pop()
#                 current_state = path[-1]  
#                 continue
#             else:
#                 break  
        
#         move = random.choice(movable) 
#         new_state = RushHour(current_state.grid_size, list(move))
        
#         explored_states.add(tuple(new_state.vehicles))
     
    
#         print(f"\nIteration {iterations}: New state chosen")
#         new_state.display_grid()
        
#         path.append(new_state)
#         current_state = new_state

#     return {
#         "message": "No solution found",
#         "iterations": iterations,
#         "solvetime": time.time() - start_time
#     }


#Question 8
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
    
def DFS_using_Heuristic(rush_hour_game, max_iterations=100000, debug=False, print_solution=True):
    start_time = time.time()
    initial_key = tuple(rush_hour_game.vehicles)

    stack = [rush_hour_game]

    predecessors = {initial_key: None}
    state_instances = {initial_key: rush_hour_game}

    iterations = 0

    while stack:
        current_state = stack.pop()  # Now this will always be a RushHour object
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

        possible_moves = current_state.get_possible_moves()
        sorted_moves = sorted(possible_moves, key=lambda move: heuristic_nb_block(RushHour(current_state.grid_size, list(move))))

        for move in sorted_moves:
            new_state = RushHour(current_state.grid_size, list(move))
            new_key = tuple(new_state.vehicles)
            #check for visited state
            if new_key not in predecessors:  
                predecessors[new_key] = current_key  
                state_instances[new_key] = new_state
                stack.append(new_state)  # Corrected: Push only new_state

    elapsed_time = time.time() - start_time
    print(f"No solution found. Execution time: {elapsed_time:.4f} seconds")
    return {
        "message": "No solution found",
        "iterations": iterations,
        "solvetime": elapsed_time
    }
#question 7
def dfs_with_solution_reconstruction(rush_hour_game, max_iterations=100000, debug=False, print_solution=True):
    """
    Depth-First Search (DFS) for Rush Hour with Solution Reconstruction.
    - Uses a stack to explore moves.
    - Stores predecessors to reconstruct the shortest solution path.
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

        #
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







#question 8
#greedy best-first search
def BFS_search_with_nb_blocking_heuristic(initial_state,print_solution = True):
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
    
    initial_cost = 0
    initial_h = heuristic_nb_block(initial_state)
    initial_f = initial_cost + initial_h
    initial_state_repr = str(initial_state.vehicles)
    
    heapq.heappush(Q, (initial_f, initial_cost, next(counter), initial_state, [initial_state]))
    visited[initial_state_repr] = initial_cost

    iterations = 0
    while Q:
        iterations += 1
        elapsed_time = time.time() - start_time
        print(f"\nIteration {iterations} (Elapsed time: {elapsed_time:.2f} seconds) - Queue size: {len(Q)}")
        
     
        f, cost, _, current_state, path = heapq.heappop(Q)
        
        
        current_state.display_grid()
        
      
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
        
            
        
  
        for move in current_state.get_possible_moves():
            new_state = RushHour(current_state.grid_size, list(move))
            new_state_repr = str(new_state.vehicles)
            new_cost = cost + 1  
            
          
            if new_state_repr not in visited or new_cost < visited[new_state_repr]:
                visited[new_state_repr] = new_cost
                new_h = heuristic_nb_block(new_state)
                new_f = new_cost + new_h
                new_path = path + [new_state]
                heapq.heappush(Q, (new_f, new_cost, next(counter), new_state, new_path))
    
    print(" No solution found.")
    return "NO_SOLUTION_FOUND"




def AStar_with_chain_blockage(rush_hour_game, print_solution=True, max_iterations=100000):
    """
    A* search for Rush Hour using a chain-blockage heuristic,
    tracking visited edges as well as visited states.

    - Priority queue items: (f, g, tie_breaker, current_state, path)
    - 'visited_states' keeps track of the best g so far for each state.
    - 'visited_edges' ensures we don't re-traverse the same (old_state -> new_state).

    Returns:
       dict with {"solution": [...], "iterations": <int>, "solvetime": <float>}
       or "NO_SOLUTION_FOUND" if no path is found.
    """
    start_time = time.time()

    open_queue = []
    visited_states = {}  # state_repr -> best g found
    visited_edges = set()  # (old_state_repr, new_state_repr) for edges

    counter = itertools.count()

    # Initial cost
    initial_g = 0
    initial_h = chain_blockage_heuristic(rush_hour_game)
    initial_f = initial_g + initial_h
    init_repr = str(rush_hour_game.vehicles)

    # Push the initial state
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

        # Check if winning
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

            # 3) Create an "edge" from old -> new
            edge = (current_repr, new_state_repr)

            # If we've traversed this exact transition before, skip
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

    # If queue is empty => no solution
    elapsed_time = time.time() - start_time
    print(f"No solution found. Execution time={elapsed_time:.4f}s")
    return "NO_SOLUTION_FOUND"






###heuristic distance 
def better_heuristic_distance(state):
    """
    A better heuristic function that estimates how far the state is from the solution.
    - Distance to exit for the red car.
    - Penalizes blocking vehicles more.
    """
    red_car = next(v for v in state.vehicles if v.label == 1)  
    distance_to_exit = state.grid_size - (red_car.x + red_car.length)
    blocking_vehicles = sum(1 for v in state.vehicles if v.x > red_car.x and v.y == red_car.y)
    return distance_to_exit + 2 * blocking_vehicles 

def dfs_with_heuristic_distance(rush_hour_game, max_iterations=100000, debug=False, print_solution=True):
    """
    Performs a Depth-First Search (DFS) to solve the RushHour game using `better_heuristic()`.
    """
    start_time = time.time()
    initial_key = tuple(rush_hour_game.vehicles)

    stack = [rush_hour_game]  # DFS uses a stack (LIFO order)

    predecessors = {initial_key: None}
    state_instances = {initial_key: rush_hour_game}

    iterations = 0

    while stack:
        current_state = stack.pop()  # Now this will always be a RushHour object
        iterations += 1
        current_key = tuple(current_state.vehicles)

        if debug:
            print(f"Iteration {iterations}: Stack size = {len(stack)}, Visited states = {len(predecessors)}")

        if current_state.check_winning():
            # Backtrack to reconstruct solution path
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

        # Get possible moves and sort them based on the heuristic (best move first)
        possible_moves = current_state.get_possible_moves()
        sorted_moves = sorted(possible_moves, key=lambda move: better_heuristic_distance(RushHour(current_state.grid_size, list(move))), reverse=True)

        # Push sorted moves onto the stack (DFS structure)
        for move in sorted_moves:
            new_state = RushHour(current_state.grid_size, list(move))
            new_key = tuple(new_state.vehicles)

            if new_key not in predecessors:
                predecessors[new_key] = current_key
                state_instances[new_key] = new_state
                stack.append(new_state)  # Push all sorted moves onto the stack

    elapsed_time = time.time() - start_time
    print(f"No solution found. Execution time: {elapsed_time:.4f} seconds")
    return {
        "message": "No solution found",
        "iterations": iterations,
        "solvetime": elapsed_time
    }








### heuristic blockage penalty

def get_red_vehicle_path(state, red_vehicle):
    """
    Returns the list of positions that the red car needs to move to exit.
    """
    path = []
    red_vehicle_end = red_vehicle.x + red_vehicle.length
    for i in range(red_vehicle_end, state.grid_size + 1):  # Move right to the exit
        path.append((i, red_vehicle.y))  # The red car remains in the same row
    return path


def find_first_blocking_vehicle(state, red_vehicle_path):
    """
    Finds the first vehicle that directly blocks the red vehicle's path.
    """
    grid = state.build_grid()

    for x, y in red_vehicle_path:  
        if grid[y - 1][x - 1] not in (".", "1"):  # If the position is occupied by another vehicle
            vehicle = state.get_vehicle_at(x, y)  # Get that vehicle
            if vehicle:
                return vehicle  #  Immediately return the first blocking vehicle

    return None  # No blocking vehicle found





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

def get_blockers(state, vehicle):
    """
    Returns a list (or set) of vehicles that block 'vehicle'
    from moving in each possible direction.
    """
    blockers = set()
    directions = ["UP", "DOWN"]  # if vehicle.orientation == 'v'
    for direction in directions:
        blocked_positions = get_blocked_positions(state, vehicle, direction)
        for (x, y) in blocked_positions:
            occupant = state.get_vehicle_at(x, y)  # row=y, col=x
            if occupant and occupant != vehicle:
                blockers.add(occupant)
    return blockers

def chain_blockage_heuristic(state):
    """
    A multi-layered (chain) blockage heuristic:
    1) Find the first vehicle blocking the red car.
    2) If none, heuristic = 0.
    3) Otherwise, recursively penalize each chain of cars blocking the primary blocker.
    """
    # 1) Find the red car
    red_car = next((v for v in state.vehicles if v.label == 1), None)
    if not red_car:
        return 0  # No red car? No penalty.

    # 2) Build the path to the exit
    red_car_path = get_red_vehicle_path(state, red_car)
    
    # 3) Identify the primary blocker
    primary_blocker = find_first_blocking_vehicle(state, red_car_path)
    if not primary_blocker:
        return 0  # No one is blocking the red car => no penalty

    # 4) Penalize the chain of cars
    # e.g., +1 for the primary blocker, plus the chain cost.
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

    
    # Alternatively, you could take the maximum chain length
    penalty = 0
    for blk in blockers:
        # +1 for each immediate blocker, plus the chain behind it
        penalty += 1 + chain_penalty(state, blk, visited)

    return penalty





def dfs_with_block_penalty(rush_hour_game, max_iterations=100000, debug=False, print_solution=True):
    """
    Depth-First Search (DFS) for Rush Hour with Advanced Heuristic.
    - Prioritizes moves using advanced_heuristic().
    - Still explores all paths like DFS but intelligently sorts them.
    """
    start_time = time.time()
    initial_key = tuple(rush_hour_game.vehicles)

    stack = [rush_hour_game]  # DFS uses a stack (LIFO order)

    predecessors = {initial_key: None}
    state_instances = {initial_key: rush_hour_game}

    iterations = 0

    while stack:
        current_state = stack.pop()  # Now this will always be a RushHour object
        iterations += 1
        current_key = tuple(current_state.vehicles)

        if debug:
            print(f"Iteration {iterations}: Stack size = {len(stack)}, Visited states = {len(predecessors)}")

        if current_state.check_winning():
            # Backtrack to reconstruct solution path
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

        # Get possible moves and sort them based on the advanced heuristic (best move first)
        possible_moves = current_state.get_possible_moves()
        sorted_moves = sorted(possible_moves, key=lambda move: chain_blockage_heuristic(RushHour(current_state.grid_size, list(move))), reverse=True)

        # Push sorted moves onto the stack (DFS structure)
        for move in sorted_moves:
            new_state = RushHour(current_state.grid_size, list(move))
            new_key = tuple(new_state.vehicles)

            if new_key not in predecessors:
                predecessors[new_key] = current_key
                state_instances[new_key] = new_state
                stack.append(new_state)  # Push all sorted moves onto the stack

    elapsed_time = time.time() - start_time
    print(f"No solution found. Execution time: {elapsed_time:.4f} seconds")
    return {
        "message": "No solution found",
        "iterations": iterations,
        "solvetime": elapsed_time
    }



