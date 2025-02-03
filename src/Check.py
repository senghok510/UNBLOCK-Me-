from src.RushHour import RushHour, Vehicle




   
class Check(RushHour):
    
    def __init__(self,vehicles):
        
         super(Check).__init__(vehicles)
         
    @classmethod
    def check_file(self,file_path):
       
        """Reads the file, validates, and initializes a RushHour game."""
        with open(file_path, "r") as file:
            lines = file.readlines()

        self.grid_size = int(lines[0].strip())
        self.num_vehicles = int(lines[1].strip())
        self.vehicles = []
        
        if len(lines) != 2 + self.num_vehicles:
            raise ValueError(
                f"Mismatch in the number of vehicles: File indicates {self.num_vehicles}, "
                f"but {len(lines) - 2} vehicle descriptions are provided."
            )

        for i in range(self.num_vehicles):
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
        
            if x_cor < 1 or y_cor < 1 or x_cor > self.grid_size or y_cor > self.grid_size:
                raise ValueError(f"Vehicle {label} starts outside the grid.")
            if orientation == 'h' and x_cor + length - 1 > self.grid_size:
                raise ValueError(f"Horizontal vehicle {label} exceeds grid boundaries.")
            if orientation == 'v' and y_cor + length - 1 > self.grid_size:
                raise ValueError(f"Vertical vehicle {label} exceeds grid boundaries.")

            self.vehicles.append(Vehicle(label, orientation, length, x_cor, y_cor))

        return RushHour(self.vehicles)

        
    def checkformoves(self):
        # initialize list for possible boards
        states = []

        for vehicle in self.vehicles:
            x_position = int(vehicle.x)
            y_position = int(vehicle.y)

            # check if vehicle is oriented horizontal and if it's not on the edge of the board
            if vehicle.orientation == 'h':
                if x_position != 0:

                    # move to the left if not blocked by another vehicle
                    if self.board[y_position][x_position - 1] == '.':
                        newVehicles = self.vehicles.copy()
                        newVehicle = Vehicle(vehicle.id, x_position - 1, y_position, vehicle.orientation, vehicle.length)

                        # remove old vehicle and append moved vehicle to list
                        newVehicles.remove(vehicle)
                        newVehicles.append(newVehicle)

                        # add new list of vehicles to list of possible boards
                        states.append(newVehicles)

                if (x_position + vehicle.length - 1) != self.width - 1:

                    # move to the right if not blocked by another vehicle
                    if self.board[y_position][x_position + (vehicle.length)] == '.':
                        newVehicles = self.vehicles.copy()
                        newVehicle = Vehicle(vehicle.id, x_position + 1, y_position, vehicle.orientation, vehicle.length)

                        # remove old vehicle and append moved vehicle to list
                        newVehicles.remove(vehicle)
                        newVehicles.append(newVehicle)

                        # add new list of vehicles to list of possible boards
                        states.append(newVehicles)

            # check if vehicle is oriented vertical and if it's not on the edge of the board
            if vehicle.orientation == 'v':
                if y_position != 0:

                    # move up if not blocked by another vehicle
                    if self.board[y_position - 1][x_position] == '.':
                        newVehicles = self.vehicles.copy()
                        newVehicle = Vehicle(vehicle.id, x_position, y_position - 1, vehicle.orientation, vehicle.length)

                        # remove old vehicle and append moved vehicle to list
                        newVehicles.remove(vehicle)
                        newVehicles.append(newVehicle)

                        # add new list of vehicles to list of possible boards
                        states.append(newVehicles)

                if y_position + (vehicle.length - 1) != self.height - 1:

                    # move down if not blocked by another vehicle
                    if self.board[y_position + vehicle.length][x_position] == '.':
                        newVehicles = self.vehicles.copy()
                        newVehicle = Vehicle(vehicle.id, x_position, y_position + 1, vehicle.orientation, vehicle.length)

                        # remove old vehicle and append moved vehicle to list
                        newVehicles.remove(vehicle)
                        newVehicles.append(newVehicle)

                        # add new list of vehicles to list of possible boards
                        states.append(newVehicles)

        return states


    #      # check if the red car is at the winning position
    # def hasSolved(self):
        
    #     if 
        
        
        
        
        


    #     return False
