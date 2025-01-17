# UNBLOCK-Me-
This project focus on the Rush Hour puzzles. The goal is the help the red car to escape the traffic and reach the exit.

# Constraint of the cars:
    - Horizontal cars: can be moved left or right
    - Vertical cars : can be moved up or down
    - One move is the displacement of one car to another eligible location

# Solution: 

    - Sequence of moves (h,u,d,l,r) that allows the red car to exit

# Optimization:
 
    - Fewest possible move of the red car to reach the exit

# Set up:

    - Lengths of the cars could be of 2 or 3 units

    - An initial state of the game will be given by a file of the following format



Ex: 
6 <- size of the grid (6x6)
8 <- number of vehicle
1 h 2 2 3 <- label + orientation + length + x, y of topleft car
2 h 2 1 1
3 h 2 5 5
4 h 3 3 6
5 v 3 6 1


