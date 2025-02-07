from src.Check import Check
import src.Algorithmes as Al
from src.RushHour import RushHour

check = Check.check_file("./data/GameP01.txt")


# rush_hour_game = RushHour(check.grid_size, check.vehicles)

# possible_state = rush_hour_game.get_possible_moves()

# dfs_solution = Al.dfs(rush_hour_game)

check.display_grid()

