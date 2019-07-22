import math
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def is_divisible_by_x(arg, x):
    return (arg % x == 0)

timer = timing()

argument = 232792560
limit = 21
is_divisible = False 

while not is_divisible: 
    for factor in range(2,limit):
        if not is_divisible_by_x(argument, factor):
            print("%d is not divisble by %d" % (argument, factor))
            is_divisible = False
            break
        else:
            is_divisible = True
            print("%d is divisble by %d" % (argument, factor))
    
    if not is_divisible:
        argument = argument + 1
        print("Argument is %d" % argument)
    else:
        print("Answer is %d" % argument)

timer("Smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {}".format(argument))
