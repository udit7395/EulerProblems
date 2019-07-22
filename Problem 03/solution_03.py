import math
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def is_divisible_by_x(arg, x):
    return (arg % x == 0)

timer = timing()

argument = 600851475143
limit = int(math.sqrt(argument)) + 2
factors = []
prime_factors = []
is_divisible = False

print("Loop will run for %d times\n" % (limit))

if is_divisible_by_x(limit, 2):
    factors.append(2)

for number in range(3, limit, 2):
    if is_divisible_by_x(argument, number):
        factors.append(number)

for factor in factors:
    for number in factors:
        if not number == factor:
            if not is_divisible_by_x(factor, number):
                is_divisible = False
            else:
                is_divisible = True
                break
    if not get_divided:
        print("Prime Factor: %d" % (factor))
        prime_factors.append(factor)

print("")
timer("Largest Prime Factor is {}".format(prime_factors[len(prime_factors) - 1]))
