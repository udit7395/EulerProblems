import math
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()
factorial = 1
aggregate = 0

for index in range(1,100,1):
    factorial = factorial * index

for digits in str(factorial):
    aggregate = aggregate + int(digits)

timer("The sum of the digits in the number 100! is {}".format(aggregate))
