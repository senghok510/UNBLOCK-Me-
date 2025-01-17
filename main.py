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
    def __init__(self, grid_size, vehicles):
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

    def display_grid(self):
        """Displays the current state of the Rush Hour game."""
        print("   " + " ".join(f"{i+1:>2}" for i in range(self.grid_size))) 
        print("   " + "---" * self.grid_size) 
        for i, row in enumerate(self.grid):
            row_display = " ".join(str(cell) if cell is not None else '.' for cell in row)
            print(f"{i+1:>2} | {row_display}")  
        print("   " + "---" * self.grid_size)  

    def display_legend(self):
        """Displays a legend of vehicle labels."""
        print("\nLegend:")
        for vehicle in self.vehicles:
            print(f"Vehicle {vehicle.label}: Orientation={vehicle.orientation.upper()}, "
                  f"Length={vehicle.length}, Position=({vehicle.x}, {vehicle.y})")
      
   
def check_file(file_path):
    """Reads the file, validates, and initializes a RushHour game."""
    with open(file_path, "r") as file:
        lines = file.readlines()

    grid_size = int(lines[0].strip())
    num_vehicles = int(lines[1].strip())
    vehicles = []
    
    if len(lines) != 2 + num_vehicles:
        raise ValueError(
            f"Mismatch in the number of vehicles: File indicates {num_vehicles}, "
            f"but {len(lines) - 2} vehicle descriptions are provided."
        )

    for i in range(num_vehicles):
        vehicle = lines[i + 2].strip().split()
        label = int(vehicle[0])
        orientation = vehicle[1]
        length = int(vehicle[2])
        x_cor = int(vehicle[3])
        y_cor = int(vehicle[4])
        

        if orientation not in ('h', 'v'):
            raise ValueError(f"Invalid vehicle orientation '{orientation}' for vehicle {label}.")
        if length not in (2, 3):
            raise ValueError(f"Invalid vehicle length '{length}' for vehicle {label}.")
    
        if x_cor < 1 or y_cor < 1 or x_cor > grid_size or y_cor > grid_size:
            raise ValueError(f"Vehicle {label} starts outside the grid.")
        if orientation == 'h' and x_cor + length - 1 > grid_size:
            raise ValueError(f"Horizontal vehicle {label} exceeds grid boundaries.")
        if orientation == 'v' and y_cor + length - 1 > grid_size:
            raise ValueError(f"Vertical vehicle {label} exceeds grid boundaries.")

        vehicles.append(Vehicle(label, orientation, length, x_cor, y_cor))

    return RushHour(grid_size, vehicles)



try:
    game = check_file("./data/GameP01.txt")
    game.display_grid()  
    game.display_legend()  
    print("Game initialized successfully!")
except ValueError as e:
    print(f"Error: {e}")
