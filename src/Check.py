
from src.RushHour import RushHour, Vehicle
#Question 1: Check if a file is a valid input
class Check:
    

    @classmethod
    def check_file(cls, file_path):
        
        with open(file_path, "r") as file:
         
            lines = [line.strip() for line in file if line.strip()]
    
        
        grid_size = int(lines[0])
        num_vehicles = int(lines[1])
        
        vehicles = []
        #extract all the lines of the files 
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
            
            #Check  for invalid orientation format
            if orientation not in ('h', 'v'):
                raise ValueError(f"Invalid vehicle orientation '{orientation}' for vehicle {label} on line {line_number}.")
            if length not in (2, 3):
                raise ValueError(f"Invalid vehicle length '{length}' for vehicle {label} on line {line_number}.")
            # Check for unbound and overbound condition
            if x_cor < 1 or y_cor < 1 or x_cor > grid_size or y_cor > grid_size:
                raise ValueError(f"Vehicle {label} starts outside the grid on line {line_number}.")
            
      
            if orientation == 'h' and x_cor + length - 1 > grid_size:
                raise ValueError(f"Horizontal vehicle {label} exceeds grid boundaries on line {line_number}.")
            if orientation == 'v' and y_cor + length - 1 > grid_size:
                raise ValueError(f"Vertical vehicle {label} exceeds grid boundaries on line {line_number}.")

            vehicles.append(Vehicle(label, orientation, length, x_cor, y_cor))
              
        return RushHour(grid_size, vehicles)

   