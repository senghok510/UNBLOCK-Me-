from src.RushHour import RushHour

import random
import time

def Brute_Force_Naive(file_path, States):
    game = RushHour.check_file(file_path=file_path)
    
    start_time = time.time()
    New_State = States
    steps=0
    while True:
        New_State = RushHour(random.choice(New_State.checkformoves()))
        steps += 1
        if New_State.hasSolved():
            return {"solvetime": time.time() - start_time, "steps": steps}
 
     
    
    
    
    
    
    
    
     
    
    
     
    
    
    
    
    
    
    
    
    return shortest_path
    
    
    
    
    
    
    
    
    
    
    