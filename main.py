
import argparse
import os
import numpy as np
import sys
from datetime import datetime
from src.Check import Check
import src.Algorithmes as Al

def log_results(algorithm, files, time, iterations, times=None):
    log_file = "results_log.txt"
    with open(log_file, "a") as f:
        f.write(f"[{datetime.now()}] Algorithm: {algorithm}\n")
        f.write(f"Processed Files: {', '.join(files)}\n")
        if len(files) == 1:
            f.write(f"Iterations: {iterations}, Time: {time:.4f} seconds\n\n")
        else:
            f.write(f"Mean Iterations: {iterations}, Mean Time: {time:.4f} seconds\n")
            
            if times is not None:
                f.write(f"All Times: {times}\n")
            f.write("\n")
def run_bfs_reconstruct_solution(files):
    
    if len(files) == 1:
        game = Check.check_file(files[0])
        print("Initial Game Configuration:")
        game.display_grid()
        print("\nSearching for a solution using bfs_direct_blocking...\n")
        result = Al.bfs_reconstruct_solution(game, print_solution=True)
        print("\nSolution found!" if "solution" in result else "\nNo solution found.")
        return  result.get("solvetime"),result.get("iterations")
    else:  
        
        times, num_iterations = [], []
        for file in files:
            game = Check.check_file(file)
            print("Initial Game Configuration:")
            game.display_grid()
            print("\nSearching for a solution using bfs_reconstruct...\n")
            result = Al.bfs_reconstruct_solution(game, debug=True, print_solution=True)
            times.append(result.get('solvetime', 0))
            num_iterations.append(result.get('iterations', 0))
            print("\nSolution found!" if "solution" in result else "\nNo solution found.")
        return np.mean(times), np.mean(num_iterations),times

def run_bfs_blocking_penalty(files):
    if len(files) == 1 :
        game = Check.check_file(files[0])
        print("Initial Game Configuration:")
        game.display_grid()
        print("\nSearching for a solution using bfs_direct_blocking...\n")
        result = Al.bfs_with_blocking_penalty(game, print_solution=True)
        print("\nSolution found!" if "solution" in result else "\nNo solution found.")
        return result.get("solvetime"),result.get("iterations") 
    times, num_iterations = [], []
    for file in files:
        game = Check.check_file(file)
        print("Initial Game Configuration:")
        game.display_grid()
        print("\nSearching for a solution using bfs_blocking_penalty...\n")
        result = Al.bfs_with_blocking_penalty(game, print_solution=True)
        times.append(result.get('solvetime', 0))
        num_iterations.append(result.get('iterations', 0))
        print("\nSolution found!" if "solution" in result else "\nNo solution found.")
    return np.mean(times), np.mean(num_iterations),times

def run_bfs_direct_blocking(files):
    
    if len(files) == 1 :
        
        game = Check.check_file(files[0])
        print("Initial Game Configuration:")
        game.display_grid()
        print("\nSearching for a solution using bfs_direct_blocking...\n")
        result = Al.bfs_direct_blocking(game, print_solution=True)
        print("\nSolution found!" if "solution" in result else "\nNo solution found.")
        return result.get("solvetime"), result.get("iterations") 
    else:
        times, num_iterations = [], []
        for file in files:
            game = Check.check_file(file[0])
            print("Initial Game Configuration:")
            game.display_grid()
            print("\nSearching for a solution using BFS with Blocking Heuristic...\n")
            result = Al.bfs_direct_blocking(game, print_solution=True)
            times.append(result.get('solvetime', 0))
            num_iterations.append(result.get('iterations', 0))
            print("\nSolution found!" if "solution" in result else "\nNo solution found.")
        return np.mean(times), np.mean(num_iterations),times



def main():
    parser = argparse.ArgumentParser(description="Run RushHour BFS variants with different heuristics.")
    parser.add_argument(
        "--algorithm",
        choices=["bfs_reconstruct", "bfs_blocking_penalty", "bfs_direct_blocking"],
        required=True,
        help="Choose the search algorithm to run."
    )
    parser.add_argument(
        "--data_path",
        type=str,
        required=True,
        help="Path to a single game file or directory containing game files."
    )
    
    args = parser.parse_args()
    
    if os.path.isdir(args.data_path):
        files = [
            os.path.join(args.data_path, f)
            for f in os.listdir(args.data_path)
            if f.endswith(".txt")
        ]
    else:
        files = [args.data_path]
    if len(files) == 1:
        if args.algorithm == "bfs_reconstruct":
            time, iterations = run_bfs_reconstruct_solution(files)
        elif args.algorithm == "bfs_blocking_penalty":
            time, iterations = run_bfs_blocking_penalty(files)
        elif args.algorithm == "bfs_direct_blocking":
            time, iterations = run_bfs_direct_blocking(files)
        print(f"\nIterations: {iterations}")
        print(f"Time: {time:.4f} seconds")
        log_results(args.algorithm,files,time,iterations)
    else:
        if args.algorithm == "bfs_reconstruct":
            mean_time, mean_iterations,times = run_bfs_reconstruct_solution(files)
        elif args.algorithm == "bfs_blocking_penalty":
            mean_time, mean_iterations,times = run_bfs_blocking_penalty(files)
        elif args.algorithm == "bfs_direct_blocking":
            mean_time, mean_iterations,times = run_bfs_direct_blocking(files)
        print(f"\nMean Iterations: {mean_iterations}")
        print(f"Mean Time: {mean_time:.4f} seconds")
        log_results(args.algorithm, files, mean_time, mean_iterations,times)
        

if __name__ == "__main__":
    main()







