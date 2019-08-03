import time
import math

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def get_prime_numbers(n, inStringFormat = False):
    p = 2
    input_array = [1] * n
    for index in range(2, int(math.sqrt(n)) + 1):
        if input_array[index] is 1:
            for temp in range(p*2, n, p):
                input_array[temp] = 0
        p = p + 1

    if inStringFormat:
        prime_numbers = list(str(index) for index in range(2, n) if input_array[index])
    else:
        prime_numbers = list(index for index in range(2, n) if input_array[index])

    return prime_numbers

timer = timing()    
limit = 1000000
prime_numbers = get_prime_numbers(limit)
limit_distinct_factors = 4
numbers = list(number for number in range(limit))
check_next = 0

for index, number in enumerate(numbers):
    distinct_factors = 0
    for i in range(0, int(math.sqrt(number))):
        if number % prime_numbers[i] == 0:
            distinct_factors += 1
    if check_next > 0:
        if distinct_factors == limit_distinct_factors:
            check_next += 1
            if check_next == limit_distinct_factors:
                timer("The first four consecutive integers to have four distinct prime factors each are {}".format(str(numbers[index + 1 - limit_distinct_factors : index + 1])[1:-1]))
                break
        else:
            check_next = 0
    elif distinct_factors == limit_distinct_factors:
        check_next += 1
