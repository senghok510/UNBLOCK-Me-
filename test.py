
import argparse
import os
import numpy as np
import sys
from datetime import datetime
from src.Check import Check
import src.Algorithmes as Al






game = Check.check_file("./data/GameP04.txt")
red_car = None
for vehicle in game.vehicles:
    if vehicle.label == 1:
        red_car = vehicle
        
        

game.display_grid()

print(Al.bfs_with_blocking_penalty(game))




