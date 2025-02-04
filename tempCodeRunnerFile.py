from src.Check import Check
import src.Algorithmes as Al
from src.RushHour import RushHour

check = Check.check_file("./data/GameP03.txt")


rush_hour_game = RushHour(check.grid_size, check.vehicles)

possible_state = rush_hour_game.check_possible_move()



result = Al.Brute_Force(rush_hour_game, possible_state)

# print(check.vehicles)
