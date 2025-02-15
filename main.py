# from src.Check import Check
# import src.Algorithmes as Al
# from src.RushHour import RushHour
# import os
# import numpy as np
# import sys





# def BFS():
#     path = "./data"
#     files = os.listdir(path)
#     files = [f for f in files if os.path.isfile(os.path.join(path, f))]
#     time = []
#     num_iterations = []
#     for file in files:
#         file = "./data/" + file
#         game = Check.check_file(file)
        
#         print("Initial Game Configuration:")
#         game.display_grid()
        
    
#         print("\nSearching for a solution using DFS...\n")
#         dfs_result = Al.bfs(game, debug=True, print_solution=True)
#         time.append(dfs_result.get('solvetime'))
#         num_iterations.append(dfs_result.get('iterations'))
#         if "solution" in dfs_result:
#             print("\nSolution found!")
#         else:
#             print("\nNo solution found.")
        
        
#     return time, num_iterations
# if __name__ == "__main__":
#     time, nb_it = BFS()
#     moyen_time = np.mean(time)
#     moyen_nb_it = np.mean(nb_it)
    
#     print(moyen_nb_it,moyen_time)
 

   
# if __name__ == "__main__":
#     from src.Check import Check

#     # Load the initial game configuration from a file.
#     game = Check.check_file("./data/GameP01.txt")
    
#     print("Initial Game Configuration:")
#     game.display_grid()
    
#     # Run the BFS algorithm.
#     result = Al.bfs(game, max_iterations=100000, debug=True, print_solution=True)
    
#     if "solution" in result:
#         print("\nSolution found!")
#         print(f"Iterations: {result['iterations']}")
#         print(f"Execution time: {result['solvetime']:.4f} seconds")
#     else:
#         print("\nNo solution found.")
#         print(f"Iterations: {result['iterations']}")
#         print(f"Execution time: {result['solvetime']:.4f} seconds")


# def run_BFS_blocking_penalty_heuristic():
#     path = "./data"
#     files = os.listdir(path)
#     files = [f for f in files if os.path.isfile(os.path.join(path, f))]
#     time = []
#     num_iterations = []
#     for file in files:
#         file = "./data/" + file
#         game = Check.check_file(file)
        
#         print("Initial Game Configuration:")
#         game.display_grid()
        
    
#         print("\nSearching for a solution using DFS...\n")
#         dfs_result = Al.AStar_with_chain_blockage(game, debug=True, print_solution=True)
#         time.append(dfs_result.get('solvetime'))
#         num_iterations.append(dfs_result.get('iterations'))
#         if "solution" in dfs_result:
#             print("\nSolution found!")
#         else:
#             print("\nNo solution found.")
        
        
#     return time, num_iterations
# if __name__ == "__main__":
#     time, nb_it = run_BFS_blocking_penalty_heuristic()
#     moyen_time = np.mean(time)
#     moyen_nb_it = np.mean(nb_it)
    
#     print(moyen_nb_it,moyen_time)
 



# if __name__ == "__main__":
 
#     game = Check.check_file("./data/GameP01.txt")
#     print("Initial Game Configuration:")
#     game.display_grid()
#     result = Al.bfs(game, max_iterations=100000, debug=True, print_solution=True)
    
#     if "solution" in result:
#         print("\nSolution found!")
#         print(f"Iterations: {result['iterations']}")
#         print(f"Execution time: {result['solvetime']:.4f} seconds")
#     else:
#         print("\nNo solution found.")
#         print(f"Iterations: {result['iterations']}")
#         print(f"Execution time: {result['solvetime']:.4f} seconds")



# def run_BFS_nb_blockings_heuristic():
#     path = "./data"
#     files = os.listdir(path)
#     files = [f for f in files if os.path.isfile(os.path.join(path, f))]
#     time = []
#     num_iterations = []
#     for file in files:
#         file = "./data/" + file
#         game = Check.check_file(file)
        
#         print("Initial Game Configuration:")
#         game.display_grid()
        
    
#         print("\nSearching for a solution using DFS...\n")
#         dfs_result = Al.BFS_search_with_nb_blocking_heuristic(game,  print_solution=True)
#         time.append(dfs_result.get('solvetime'))
#         num_iterations.append(dfs_result.get('iterations'))
#         if "solution" in dfs_result:
#             print("\nSolution found!")
#         else:
#             print("\nNo solution found.")
#     return time, num_iterations
# if __name__ == "__main__":
#     time, nb_it = run_BFS_nb_blockings_heuristic()
#     moyen_time = np.mean(time)
#     moyen_nb_it = np.mean(nb_it)
#     print(moyen_nb_it,moyen_time)
  



# if __name__ == "__main__":
#     game = Check.check_file("./data/GameP01.txt")  
#     game.display_grid()
#     print(Al.BFS_search_with_nb_blocking_heuristic(game))


    
  

# game = Check.check_file("./data/GameP01.txt")
# bfs = Al.bfs_reconstruct_solution(game)

# bfs_heuristic = Al.BFS_search_with_nb_blocking_heuristic(game)
# bfs_block = Al.AStar_with_chain_blockage(game)
    
# print(bfs.get("solvetime"),bfs_heuristic.get("solvetime"),bfs_block.get("solvetime"))  

import argparse
import os
import numpy as np
import sys
from src.Check import Check
import src.Algorithmes as Al

def run_bfs(files):
    times, num_iterations = [], []
    for file in files:
        game = Check.check_file(file)
        print("Initial Game Configuration:")
        game.display_grid()
        print("\nSearching for a solution using BFS...\n")
        result = Al.bfs(game, debug=True, print_solution=True)
        times.append(result.get('solvetime', 0))
        num_iterations.append(result.get('iterations', 0))
        print("\nSolution found!" if "solution" in result else "\nNo solution found.")
    return np.mean(times), np.mean(num_iterations)

def run_a_star_blocking_penalty(files):
    times, num_iterations = [], []
    for file in files:
        game = Check.check_file(file)
        print("Initial Game Configuration:")
        game.display_grid()
        print("\nSearching for a solution using A* with Blocking Penalty...\n")
        result = Al.AStar_with_chain_blockage(game, debug=True, print_solution=True)
        times.append(result.get('solvetime', 0))
        num_iterations.append(result.get('iterations', 0))
        print("\nSolution found!" if "solution" in result else "\nNo solution found.")
    return np.mean(times), np.mean(num_iterations)

def run_bfs_blocking_heuristic(files):
    times, num_iterations = [], []
    for file in files:
        game = Check.check_file(file)
        print("Initial Game Configuration:")
        game.display_grid()
        print("\nSearching for a solution using BFS with Blocking Heuristic...\n")
        result = Al.BFS_search_with_nb_blocking_heuristic(game, print_solution=True)
        times.append(result.get('solvetime', 0))
        num_iterations.append(result.get('iterations', 0))
        print("\nSolution found!" if "solution" in result else "\nNo solution found.")
    return np.mean(times), np.mean(num_iterations)

def main():
    parser = argparse.ArgumentParser(description="Run RushHour BFS variants with different heuristics.")
    parser.add_argument("--algorithm", choices=["bfs", "a_star_block", "bfs_block"], required=True,
                        help="Choose the search algorithm to run.")
    parser.add_argument("--data_path", type=str, required=True,
                        help="Path to a single game file or directory containing game files.")
    
    args = parser.parse_args()
    
    if os.path.isdir(args.data_path):
        files = [os.path.join(args.data_path, f) for f in os.listdir(args.data_path) if f.endswith(".txt")]
    else:
        files = [args.data_path]
    
    if args.algorithm == "bfs":
        mean_time, mean_iterations = run_bfs(files)
    elif args.algorithm == "a_star_block":
        mean_time, mean_iterations = run_a_star_blocking_penalty(files)
    elif args.algorithm == "bfs_block":
        mean_time, mean_iterations = run_bfs_blocking_heuristic(files)
    
    print(f"\nMean Iterations: {mean_iterations}, Mean Time: {mean_time:.4f} seconds")

if __name__ == "__main__":
    main()

