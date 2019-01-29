import math
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def is_divisible_by_x(arg, x):
    return (arg % x == 0)

timer = timing()
limit = 10001
prime_numbers = [3, 5, 7, 11, 13]
index = 15
is_divisble = False

while len(prime_numbers) < limit:
    loop_limit = math.sqrt(index) + 1
    for prime_number in prime_numbers:
        if(prime_number > loop_limit):
            break

        if(is_divisible_by_x(index, prime_number)):
            is_divisble = True
            break
        else:
            is_divisble = False

    if not is_divisble:
        prime_numbers.append(index)

    index = index + 2

timer("The {} prime number is {}".format(limit, prime_numbers[limit - 1]))
