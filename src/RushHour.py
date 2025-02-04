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
   
    

class RushHour:
    
    def __init__(self, grid_size,vehicles):
        
        self.grid_size = grid_size
        self.vehicles = vehicles  
        self.grid = [[None] * grid_size for _ in range(grid_size)]  
        self._place_vehicles_on_grid()
    # Question 2: 
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

    # Question 4: check all possible move 
    def check_possible_move(self):
        """Returns all possible vehicle moves."""
        possible_moves = set()  # Set to store unique possible states

        for vehicle in self.vehicles:
            x_pos = vehicle.x - 1  
            y_pos = vehicle.y - 1  # Convert to 0-based index
               # Move vertical vehicle
            if vehicle.orientation == 'v':
                # Can move up
                if y_pos > 0 and self.grid[y_pos - 1][x_pos] == ".":
                    updated_vehicles = copy.deepcopy(self.vehicles)
                    moved_vehicle = Vehicle(vehicle.label, vehicle.orientation, vehicle.length, vehicle.x, vehicle.y - 1)
                   
                    for i, v in enumerate(updated_vehicles):
                        if v.label == vehicle.label:
                            updated_vehicles[i] = moved_vehicle
                            break
                    possible_moves.add(frozenset(updated_vehicles)) 

                # Can move down
                if (y_pos + vehicle.length) < self.grid_size and self.grid[y_pos + vehicle.length][x_pos] == ".":
                    updated_vehicles = copy.deepcopy(self.vehicles)
                    moved_vehicle = Vehicle(vehicle.label, vehicle.orientation, vehicle.length, vehicle.x, vehicle.y + 1)
                 
                    for i, v in enumerate(updated_vehicles):
                        if v.label == vehicle.label:
                            updated_vehicles[i] = moved_vehicle
                            break
                    possible_moves.add(frozenset(updated_vehicles)) 


            # Move horizontal vehicle
            elif vehicle.orientation == 'h':
                # Can move left
                if x_pos > 0 and self.grid[y_pos][x_pos - 1] == ".":
                    updated_vehicles = copy.deepcopy(self.vehicles)
                    moved_vehicle = Vehicle(vehicle.label, vehicle.orientation, vehicle.length, vehicle.x - 1, vehicle.y)
                   
                    for i, v in enumerate(updated_vehicles):
                        if v.label == vehicle.label:
                            updated_vehicles[i] = moved_vehicle
                            break
                    possible_moves.add(frozenset(updated_vehicles)) 
                # Can move right
                if (x_pos + vehicle.length) < self.grid_size and self.grid[y_pos][x_pos + vehicle.length] == ".":
                    updated_vehicles = copy.deepcopy(self.vehicles)
                    moved_vehicle = Vehicle(vehicle.label, vehicle.orientation, vehicle.length, vehicle.x + 1, vehicle.y)
                   
                    for i, v in enumerate(updated_vehicles):
                        if v.label == vehicle.label:
                            updated_vehicles[i] = moved_vehicle
                            break
                    possible_moves.add(frozenset(updated_vehicles))  # Use frozenset to ensure hashability

         

        return possible_moves

    
    def check_winning(self):
        """Checks if the red car has reached the winning position."""
        
        for vehicle in self.vehicles:
          
            if vehicle.label == 1:
                # The target position for the red car (usually at grid_size-2, grid_size // 2)
                target_x = self.grid_size - 2
                target_y = self.grid_size // 2
                
                if vehicle.orientation == "h" and vehicle.x == target_x and vehicle.y == target_y:
                    return True  
                
        return False  


    def __hash__(self):
        """Make Vehicle hashable."""
        return hash((self.label, self.orientation, self.length, self.x, self.y))
    
    def __eq__(self, other):
        """Ensure equality check works properly."""
        return (self.label, self.orientation, self.length, self.x, self.y) == (
            other.label, other.orientation, other.length, other.x, other.y
        )


