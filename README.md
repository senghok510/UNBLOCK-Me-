# UNBLOCK-Me-
This project focus on the Rush Hour puzzles. The goal is the help the red car to escape the traffic and reach the exit.
# Constraint of the cars:
    - Horizontal cars: can be moved left or right
    - Vertical cars : can be moved up or down
    - One move is the displacement of one car to another eligible location
Ex: 
6 <- size of the grid (6x6)
8 <- number of vehicle
1 h 2 2 3 <- label + orientation + length + x, y of topleft car
2 h 2 1 1
3 h 2 5 5
4 h 3 3 6
5 v 3 6 1

# Brute Force approach with reconstruction solution

Firstly, we implement the Breadth-first Search to solve the game by visiting all the possible moves , when we find the solution , we reconstruct the solution.

# Heuristic using the number of vehicles between the red vehicle and the exit:
In this heuristic, we count the number of vihicles between the red vehicle and the exit each moves of the game. This approach helps us to improve the time of execution.

# Heuristic by counting the number of the vehicle that block the first-blocking vehicle chainly


# Library, in case you haven't installed some necessary libraries , please go to the file requirements.txt and run in the terminal using:
 'pip install -r library_name'


# Here are some way to run the program

- The project directory is spllited into two main sections. The folder 'src' contains all the necessary classes to build the game. There is a 
'main.py' where all the task are located.

In the 'main.py', the readers are invited to write the following line in the terminal to run a specific algorithm on a specific testing file that
in the 'data' folder.

In the Terminal, there are three mains algorithms: ["bfs_reconstruct", "bfs_blocking_penalty", "bfs_direct_blocking"]

* Run a specific file: 'python main.py --algorithm algortihm_name --data_path ./data/file_name.txt'
* Run the whole file to investigate mean execution time : 'python main.py --algorithm algorithm_name --data_path ./data/'

Finally, the user can see the stocked results each execution in the file 'results_log.txt'.

Enjoy testing the project :)

