import copy

class Vehicle:
    def __init__(self, label, orientation, length, x, y):
        self.label = label
        self.orientation = orientation  
        self.length = length
        self.x = x  
        self.y = y  
    def get_positions(self):
        """
        Returns all grid positions (as (x, y) tuples, 1-indexed)
        occupied by this vehicle.
        """
        return [
            (self.x + i if self.orientation == "h" else self.x,
             self.y + i if self.orientation == "v" else self.y)
            for i in range(self.length)
        ]

   

    def __hash__(self):
        return hash((self.label, self.orientation, self.length, self.x, self.y))

    def __eq__(self, other):
        return (self.label, self.orientation, self.length, self.x, self.y) == (
            other.label, other.orientation, other.length, other.x, other.y
        )
    
    def __repr__(self):
        return f"Vehicle({self.label}, '{self.orientation}', {self.length}, {self.x}, {self.y})"


class RushHour:
    def __init__(self, grid_size, vehicles):
        self.grid_size = grid_size
        self.vehicles = vehicles  
     # Question 2: the methods that display the state of the RushHour game 
    def build_grid(self, vehicles=None):
      
        if vehicles is None:
            vehicles = self.vehicles
      
        grid = [["." for _ in range(self.grid_size)] for _ in range(self.grid_size)]
    
        for vehicle in vehicles:
            for x, y in vehicle.get_positions():
                if not (1 <= x <= self.grid_size and 1 <= y <= self.grid_size):
                    raise ValueError(f"Vehicle {vehicle.label} goes out of grid bounds at ({x}, {y}).")
                if grid[y - 1][x - 1] != ".":
                    raise ValueError(f"Invalid input: Overlapping vehicles at ({x}, {y}).")
                grid[y - 1][x - 1] = str(vehicle.label)
        return grid

    def display_grid(self):
        """Displays the current state of the grid."""
        grid = self.build_grid()
        header = "   " + " ".join(f"{i+1:>2}" for i in range(self.grid_size))
        separator = "   " + "---" * self.grid_size
        print(header)
        print(separator)
        for i, row in enumerate(grid):
            row_display = "  ".join(cell for cell in row)
            print(f"{i+1:>2} | {row_display}")
        print(separator)
     # Question 4: Returns all the possible moves of a given state
    def get_possible_moves(self):
      
        possible_moves = set() #to store unique elements
        grid = self.build_grid()  

        
        def create_new_state(vehicle, new_x, new_y):
            new_state = []
            for v in self.vehicles:
                if v.label == vehicle.label:
                    new_state.append(Vehicle(v.label, v.orientation, v.length, new_x, new_y))
                else:
                    new_state.append(copy.deepcopy(v))
            return tuple(new_state)

        for vehicle in self.vehicles:
       
            x_index = vehicle.x - 1
            y_index = vehicle.y - 1

            if vehicle.orientation == 'v':
                # Move up
                if y_index > 0 and grid[y_index - 1][x_index] == ".":
                    possible_moves.add(create_new_state(vehicle, vehicle.x, vehicle.y - 1))
                # Move down
                bottom_index = y_index + vehicle.length - 1
                if bottom_index < self.grid_size - 1 and grid[bottom_index + 1][x_index] == ".":
                    possible_moves.add(create_new_state(vehicle, vehicle.x, vehicle.y + 1))
            elif vehicle.orientation == 'h':
                # Move left
                if x_index > 0 and grid[y_index][x_index - 1] == ".":
                    possible_moves.add(create_new_state(vehicle, vehicle.x - 1, vehicle.y))
                # Move right
                right_index = x_index + vehicle.length - 1
                if right_index < self.grid_size - 1 and grid[y_index][right_index + 1] == ".":
                    possible_moves.add(create_new_state(vehicle, vehicle.x + 1, vehicle.y))
        return possible_moves

    def check_winning(self):
        
        for vehicle in self.vehicles:
            if vehicle.label == 1 and vehicle.orientation == "h":
                rightmost = vehicle.x + vehicle.length - 1
                if rightmost == self.grid_size:
                    return True
        return False
