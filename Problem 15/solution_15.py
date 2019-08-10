import time
import math

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()
grid_size = 20
number_of_routes = math.factorial((grid_size * 2)) // (math.factorial(grid_size) * math.factorial(grid_size))

timer("Starting in the top left corner of a {}×{} grid, only being able to move to the right and down, there are exactly {} routes to the bottom right corner".format(grid_size, grid_size, number_of_routes)) 
