import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()

summation = 0
limit = 1000
div_3 = 3
div_5 = 5

def is_divisible_by_x(arg, x):
    return (arg % x == 0)

for number in range(limit):
    if is_divisible_by_x(number, div_3) or is_divisible_by_x(number, div_5):
        summation = summation + number

timer("Sum of all the multiples of {} or {} below {} is {}".format(div_3, div_5, limit, summation))
