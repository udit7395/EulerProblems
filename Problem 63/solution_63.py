import time
import math

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()
power_limit = 10 ** 2
number_limit = 9
counter = 0

for power in range(1, power_limit):
    for number in range(1, number_limit + 1):
        len_output = len(str(number ** power))
        if len_output == power:
            counter += 1
        elif len_output >= power:
            break

timer("There are {} n-digit positive integers exist which are also an nth power".format(counter))
