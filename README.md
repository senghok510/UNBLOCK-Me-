# UNBLOCK-Me

This project focuses on solving **Rush Hour puzzles**. The goal is to help the red car escape the traffic and reach the exit.

## Constraints of the Cars

- **Horizontal cars**: Can be moved left or right.
- **Vertical cars**: Can be moved up or down.
- **One move**: The displacement of one car to another eligible location.

---
## Brute Force Approach with Solution Reconstruction

The **Breadth-First Search (BFS)** algorithm is implemented to solve the puzzle by exploring all possible moves.  
When a solution is found, we reconstruct the sequence of moves that led to the solution.
---

## Heuristics to Improve Execution Time

### 1. **Heuristic using the number of vehicles between the red vehicle and the exit**
- This heuristic counts the number of vehicles blocking the red car's path to the exit.
- The fewer blocking vehicles, the better the move.
- This approach significantly reduces execution time.

### 2. **Heuristic by counting the number of vehicles blocking the first-blocking vehicle**
- Instead of only counting vehicles between the red vehicle and the exit, this heuristic considers **chained blocking vehicles** which penalize the vehicle recursively that block vertically 
the first blocking vehicle that block the red vehicle.
All the functions are located in the Algorithmes.py in src
---

## How to run the project

If some necessary libraries are missing, install them using the `requirements.txt` file:
pip install -r requirements.txt


# How to Run the Program

The project directory is split into two main sections:

- **`src/` folder** — contains all the classes needed to build the game and the three algorithms 
- **`main.py`** — the main execution script.

## Running Algorithms

To run a **specific algorithm** on a **single test file**
Put the following command in the terminal:
'python main.py --algorithm algorithm_name --data_path ./data/file_name.txt'

To Run All Test Files and Calculate Mean Execution Time
Put the following command in the terminal:

'python main.py --algorithm algorithm_name --data_path ./data/'

- algorithm_name is to be chosen from:
["bfs_reconstruct", "bfs_blocking_penalty", "bfs_direct_blocking"]
- for example if one want to run a specific file  : 
'python main.py --algorithm bfs_reconstruct --data_path ./data/GameP01.txt'
or 'python main.py --algorithm bfs_reconstruct --data_path ./data/' to run on all the files inside the data folder.


## Checking Results

All runs log their results in **`results_log.txt`**.

---

## Enjoy Testing the Project!

Feel free to experiment with different heuristics and approaches to see how they affect both speed and solution quality.
