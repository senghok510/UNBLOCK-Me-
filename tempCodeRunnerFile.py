from src.Check import Check
import src.Algorithmes as Al
from src.RushHour import RushHour

check = Check.check_file("./data/GameP03.txt")


rush_hour_game = RushHour(check.grid_size, check.vehicles)

possible_state = rush_hour_game.check_possible_move()

state1= possible_state.pop()
state2 = possible_state.pop()
dfs_solution = Al.DFS(rush_hour_game)


# print(type(state1))



# vehicles = list(state1)

# new_rush_hour_game = RushHour(rush_hour_game.grid_size,vehicles)

# new_rush_hour_game.display_grid()

# state1 = possible_state.pop()
# print(check.display_grid())
# if isinstance(state1, frozenset):
#     # Unfreeze the frozenset by converting it to a regular set
#     mutable_state = set(state1)


#     vehicles = list(mutable_state)  
#     new_rush_hour_game = RushHour(rush_hour_game.grid_size, vehicles)


#     print(new_rush_hour_game.display_grid())
# else:
#     print("State is not a frozenset.")

# state2 = possible_state.pop()
# if isinstance(state2, frozenset):
#     # Unfreeze the frozenset by converting it to a regular set
#     mutable_state = set(state2)

#     vehicles = list(mutable_state) 
#     new_rush_hour_game = RushHour(rush_hour_game.grid_size, vehicles)


#     print(new_rush_hour_game.display_grid())
# else:
#     print("State is not a frozenset.")

