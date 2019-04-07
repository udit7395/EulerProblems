import math 
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()

power = 5
lower_limit = 10
upper_limit = 999999
final_aggregate = 0

for number in range(lower_limit, upper_limit):
    aggregate = 0
    for digit in str(number):
        aggregate += (int(digit) ** power)
    if number == aggregate:
        final_aggregate += number

timer("The sum of all the numbers that can be written as the sum of fifth powers of their digits is {}".format(final_aggregate))