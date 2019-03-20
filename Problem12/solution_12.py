import math
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def sum_upto_n_numbers(limit):
    return (limit * (limit + 1)) * 0.5

def is_divisible_by_x(arg, x):
    return (arg % x == 0)

timer = timing()

limit = 7
divisors = []

aggregate = int(sum_upto_n_numbers(limit))

while(len(divisors) * 2 < 501):
    aggregate = int(sum_upto_n_numbers(limit))
    print("Aggregate : %d" % aggregate)    
    print("Limit : %d" % limit)
    divisors.clear()
    divisors.append(1)
    for number in range(2, int(math.sqrt(aggregate) + 1)):
        if(is_divisible_by_x(aggregate, number)):
            divisors.append(number)  
    divisors.append(aggregate)
    limit = limit + 1
    print("Divisor  : {}".format(divisors))
    print("Divisor len : %d" % len(divisors))
    print("")

timer("The value of the first triangle number to have over five hundred divisors is {}".format(aggregate))