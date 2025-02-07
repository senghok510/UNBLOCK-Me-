# from src.RushHour import RushHour, Vehicle
# import copy



   
# class Check(RushHour):
    
#     def __init__(self,vehicles):
        
#          super(Check).__init__(vehicles)
         
#     @classmethod
#     # Question 1: method that check file 
#     def check_file(self,file_path):
       
#         """Reads the file, validates, and initializes a RushHour game."""
#         with open(file_path, "r") as file:
#             lines = file.readlines()

#         self.grid_size = int(lines[0].strip())
#         self.num_vehicles = int(lines[1].strip())
#         self.vehicles = []
        
#         if len(lines) != 2 + self.num_vehicles:
#             raise ValueError(
#                 f"Mismatch in the number of vehicles: File indicates {self.num_vehicles}, "
#                 f"but {len(lines) - 2} vehicle descriptions are provided."
#             )

#         for i in range(self.num_vehicles):
#             vehicle = lines[i + 2].strip().split()
#             label = int(vehicle[0])
#             orientation = vehicle[1]
#             length = int(vehicle[2])
#             x_cor = int(vehicle[3])
#             y_cor = int(vehicle[4])
            
#             if orientation not in ('h', 'v'):
#                 raise ValueError(f"Invalid vehicle orientation '{orientation}' for vehicle {label}.")
#             if length not in (2, 3):
#                 raise ValueError(f"Invalid vehicle length '{length}' for vehicle {label}.")
        
#             if x_cor < 1 or y_cor < 1 or x_cor > self.grid_size or y_cor > self.grid_size:
#                 raise ValueError(f"Vehicle {label} starts outside the grid.")
#             if orientation == 'h' and x_cor + length - 1 > self.grid_size:
#                 raise ValueError(f"Horizontal vehicle {label} exceeds grid boundaries.")
#             if orientation == 'v' and y_cor + length - 1 > self.grid_size:
#                 raise ValueError(f"Vertical vehicle {label} exceeds grid boundaries.")

#             self.vehicles.append(Vehicle(label, orientation, length, x_cor, y_cor))

#         return RushHour(self.grid_size,self.vehicles)
    
from src.RushHour import RushHour, Vehicle

class Check:

    @classmethod
    def check_file(cls, file_path):
        
        with open(file_path, "r") as file:
         
            lines = [line.strip() for line in file if line.strip()]
    
        try:
            grid_size = int(lines[0])
            num_vehicles = int(lines[1])
        except (IndexError, ValueError) as e:
            raise ValueError("Invalid file format for grid size or number of vehicles.") from e

        if len(lines) != 2 + num_vehicles:
            raise ValueError(
                f"Mismatch in the number of vehicles: File indicates {num_vehicles}, "
                f"but {len(lines) - 2} vehicle descriptions are provided."
            )
        
        vehicles = []
    
        for i in range(num_vehicles):
            line_number = i + 3  
            parts = lines[i + 2].split()
            if len(parts) != 5:
                raise ValueError(f"Invalid vehicle description format on line {line_number}.")
            
            try:
                label = int(parts[0])
                orientation = parts[1].lower() 
                length = int(parts[2])
                x_cor = int(parts[3])
                y_cor = int(parts[4])
            except ValueError as e:
                raise ValueError(f"Invalid vehicle data on line {line_number}.") from e
            
           
            if orientation not in ('h', 'v'):
                raise ValueError(f"Invalid vehicle orientation '{orientation}' for vehicle {label} on line {line_number}.")
            if length not in (2, 3):
                raise ValueError(f"Invalid vehicle length '{length}' for vehicle {label} on line {line_number}.")
            
            if x_cor < 1 or y_cor < 1 or x_cor > grid_size or y_cor > grid_size:
                raise ValueError(f"Vehicle {label} starts outside the grid on line {line_number}.")
            
      
            if orientation == 'h' and x_cor + length - 1 > grid_size:
                raise ValueError(f"Horizontal vehicle {label} exceeds grid boundaries on line {line_number}.")
            if orientation == 'v' and y_cor + length - 1 > grid_size:
                raise ValueError(f"Vertical vehicle {label} exceeds grid boundaries on line {line_number}.")

            vehicles.append(Vehicle(label, orientation, length, x_cor, y_cor))
        
        return RushHour(grid_size, vehicles)

   