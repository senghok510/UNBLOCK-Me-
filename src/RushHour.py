import copy
from math import ceil

class Vehicle:
    def __init__(self, label, orientation, length, x, y):
        self.label = label
        self.orientation = orientation
        self.length = length
        self.x = x
        self.y = y

    def Position_vehicle(self):
        """Returns all the grid positions occupied by this vehicle."""
        position = []
        for i in range(self.length):
            if self.orientation == "v": 
                position.append((self.x, self.y + i))
            elif self.orientation == "h":  
                position.append((self.x + i, self.y))
        return position
   
    
class Dimension():
    def init():
        global grid_size

class RushHour:
    def __init__(self, vehicles):
       
        self.grid_size = grid_size
        self.vehicles = vehicles  
        self.grid = [[None] * grid_size for _ in range(grid_size)]  
        self._place_vehicles_on_grid()

    def _place_vehicles_on_grid(self):
        """Places vehicles on the grid and checks for overlaps."""
        for vehicle in self.vehicles:
            for x, y in vehicle.Position_vehicle():
                
                if x < 1 or y < 1 or x > self.grid_size or y > self.grid_size:
                    raise ValueError(f"Vehicle {vehicle.label} goes out of grid bounds at ({x}, {y}).")
               
                if self.grid[y - 1][x - 1] is not None:
                    raise ValueError(f"Invalid input: Overlapping vehicles at ({x}, {y}).")
              
                self.grid[y - 1][x - 1] = vehicle.label
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == None:
                    self.grid[i][j] = "."
    def display_grid(self):
        """Displays the current state of the Rush Hour game."""
        print("   " + " ".join(f"{i+1:>2}" for i in range(self.grid_size))) 
        print("   " + "---" * self.grid_size) 
        for i, row in enumerate(self.grid):
            row_display = "  ".join(str(cell) if cell is not None else '.' for cell in row)
            print(f"{i+1:>2} | {row_display}")  
        print("   " + "---" * self.grid_size)  

    def display_legend(self):
        """Displays a legend of vehicle labels."""
        print("\nLegend:")
        for vehicle in self.vehicles:
            print(f"Vehicle {vehicle.label}: Orientation={vehicle.orientation.upper()}, "
                  f"Length={vehicle.length}, Position=({vehicle.x}, {vehicle.y})")
   
