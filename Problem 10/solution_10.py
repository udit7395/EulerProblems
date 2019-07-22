import math
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def is_divisible_by_x(arg, x):
    return (arg % x == 0)

timer = timing()
limit = 2000000
prime_numbers = [3, 5, 7]
index = 9
is_divisble = False

while index < limit:
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


prime_numbers.append(2)
timer("sum of all the primes below {} is {}".format(limit, sum(prime_numbers)))
