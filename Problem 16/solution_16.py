import math
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def inner_sum(arg):
    summation  = 0 
    for index in range(0, len(arg)):
        summation = summation + int(arg[index])
    return summation

timer = timing()

argument = 2 
limit = 1000

timer("The sum of the digits of the number {}^{} is {}".format(argument,limit,inner_sum(str(int(math.pow(argument, limit))))))
