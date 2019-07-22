import math 
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def getLimit(argument):
    limit = "1"
    for i in range(argument -1):
        limit += "0"
    return int(limit)

timer = timing()

last_term = 0
index = 2
fibonnaci_series = [1,1]
input_limit = 1000

while(last_term < getLimit(input_limit)):
    last_term = fibonnaci_series[index - 1] + fibonnaci_series[index - 2]
    fibonnaci_series.append(last_term)
    index += 1

timer("The index of the first term in the Fibonacci sequence to contain 1000 digits is {}".format(index))