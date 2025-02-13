from src.Check import Check
import src.Algorithmes as Al
from src.RushHour import RushHour
import os
import numpy as np






# def run_Brute_Force_random():  
#     game = Check.check_file("./data/GameP01.txt")
    
 
#     print("Initial Game Configuration:")
#     game.display_grid()
    
   
#     result = Al.random(game, max_iterations=10000)
    
   
#     if "solution" in result:
#         print("\nSolution found!")
#         print("Number of iterations:", result["iterations"])
#         print("Execution time: {:.4f} seconds".format(result["solvetime"]))
#         print("\n--- Solution Path ---")
      
#         for step, state in enumerate(result["solution"]):
#             print(f"\nStep {step}:")
#             state.display_grid()
#     else:
#         print("\nNo solution found.")
#         print("Iterations performed:", result["iterations"])
#         print("Execution time: {:.4f} seconds".format(result["solvetime"]))


# def run_DFS():
#     path = "./data"
#     files = os.listdir(path)
#     files = [f for f in files if os.path.isfile(os.path.join(path, f))]
#     time = []
#     num_iterations = []
#     iter_file = 0
#     for file in files:
#         file = "./data/" + file

#         game = Check.check_file(file)
    
   
#         print("Initial Game Configuration:")
#         game.display_grid()
        
    
#         print("\nSearching for a solution using DFS...\n")
#         iter_file += 1
#         print(iter_file)
#         dfs_result = Al.dfs(game, debug=True, print_solution=True)
#         time.append(dfs_result.get("solvetime"))
#         num_iterations.append(dfs_result.get("iterations"))
        
#         if "solution" in dfs_result:
#             print(f"\nSolution found!,{iter_file}")
#         else:
#             print("\nNo solution found.")
#     return time, num_iterations
# # ensure that the code is only executed directly when the script is run, when you import the file main.py into another file: it will not be run 
# # automatically

# if __name__ == "__main__":
#     time , num_it = run_DFS()
#     print(f"mean and tiime:{np.mean(time), np.mean(num_it)}")
    
    

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
# if __name__ == "__main__":


#     # Load the initial game configuration from a file.
#     game = Check.check_file("./data/GameP01.txt")
    
#     print("Initial Game Configuration:")
#     game.display_grid()
    
#     # Run the A* search.
#     result = Al.a_star(game, max_iterations=100000, debug=True, print_solution=True)
    
#     if "solution" in result:
#         print("\nSolution found!")
#         print(f"Iterations: {result['iterations']}")
#         print(f"Execution time: {result['solvetime']:.4f} seconds")
#     else:
#         print("\nNo solution found.")
#         print(f"Iterations: {result['iterations']}")
#         print(f"Execution time: {result['solvetime']:.4f} seconds")




# def run_DFS_heuristic_distance():
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
#         dfs_result = Al.dfs_with_heuristic_distance(game, debug=True, print_solution=True)
#         time.append(dfs_result.get('solvetime'))
#         num_iterations.append(dfs_result.get('iterations'))
#         if "solution" in dfs_result:
#             print("\nSolution found!")
#         else:
#             print("\nNo solution found.")
        
        
#     return time, num_iterations
# if __name__ == "__main__":
#     time, nb_it = run_DFS_heuristic_distance()
#     moyen_time = np.mean(time)
#     moyen_nb_it = np.mean(nb_it)
    
#     print(moyen_nb_it,moyen_time)
    
    
    
  
    


# def run_DFS_blocking_penalty_heuristic():
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
#         dfs_result = Al.dfs_with_block_penalty(game, debug=True, print_solution=True)
#         time.append(dfs_result.get('solvetime'))
#         num_iterations.append(dfs_result.get('iterations'))
#         if "solution" in dfs_result:
#             print("\nSolution found!")
#         else:
#             print("\nNo solution found.")
        
        
#     return time, num_iterations
# if __name__ == "__main__":
#     time, nb_it = run_DFS_blocking_penalty_heuristic()
#     moyen_time = np.mean(time)
#     moyen_nb_it = np.mean(nb_it)
    
#     print(moyen_nb_it,moyen_time)
    
# # game = Check.check_file("./data/GameP01.txt")  
# # game.display_grid()
# # for vehicle in game.vehicles:
# #     if vehicle.label == 1:
# #         red_car = vehicle
# # path = Al.get_red_vehicle_path(game,red_car)      
# # first = Al.find_first_blocking_vehicle(game,path)
# # penalty = Al.chain_penalty(game,first,None)
# # blocker = Al.get_blockers(game,first)
# # print(Al.dfs_with_block_penalty(game))
# # # print(first)
# # # print(second)




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
#         dfs_result = Al.AStar_with_chain_blockage(game,  print_solution=True)
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
  

game = Check.check_file("./data/GameP40.txt")

print(game.display_grid())


    
  
    
