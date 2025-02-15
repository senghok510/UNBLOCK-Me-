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
- Instead of only counting vehicles between the red car and the exit, this heuristic considers **chained blocking vehicles**.
- The game prioritizes moves that remove the root cause of congestion.

---

## Required Libraries

If some necessary libraries are missing, install them using the `requirements.txt` file:

```bash
pip install -r requirements.txt
