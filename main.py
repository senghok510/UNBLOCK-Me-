from src.Check import Check
import src.Algorithmes as Al
from src.RushHour import RushHour

def run_Brute_Force_random():
    
    game = Check.check_file("./data/GameP01.txt")
    
 
    print("Initial Game Configuration:")
    game.display_grid()
    
   
    result = Al.brute_force(game, max_iterations=10000)
    
   
    if "solution" in result:
        print("\nSolution found!")
        print("Number of iterations:", result["iterations"])
        print("Execution time: {:.4f} seconds".format(result["solvetime"]))
        print("\n--- Solution Path ---")
      
        for step, state in enumerate(result["solution"]):
            print(f"\nStep {step}:")
            state.display_grid()
    else:
        print("\nNo solution found.")
        print("Iterations performed:", result["iterations"])
        print("Execution time: {:.4f} seconds".format(result["solvetime"]))





def run_DFS():

    game = Check.check_file("./data/GameP01.txt")
    
   
    print("Initial Game Configuration:")
    game.display_grid()
    
 
    print("\nSearching for a solution using DFS...\n")
    dfs_result = Al.dfs(game, debug=True, print_solution=True)
    
    if "solution" in dfs_result:
        print("\nSolution found!")
    else:
        print("\nNo solution found.")
    
    print(f"\nIterations: {dfs_result.get('iterations')}")
    print(f"Execution time: {dfs_result.get('solvetime'):.4f} seconds")
# ensure that the code is only executed directly when the script is run, when you import the file main.py into another file: it will not be run 
# automatically



# if __name__ == "__main__":
#     run_DFS()
    
    

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

game = Check.check_file("./data/GameP01.txt")


result = Al.BFS_search_with_heuristic_approach(game)

print(result)