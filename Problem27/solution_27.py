import math
import itertools 
import time

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

def check_prime_sequence(a, b):
    global sequence_length
    index = 0
    while True:
        output = index ** 2 - index * a + b
        if str(output) not in prime_numbers:
            break
        index += 1
    if index >= sequence_length:
        sequence_length = index
        return True
    else:
        return False
 
timer = timing()

prime_numbers = get_prime_numbers(10000, True)
prime_numbers_less_than_1000 = list(filter(lambda x: int(x) < 1000, prime_numbers))
quadratic_primes = [0,0]
sequence_length = 0
combinations = list(itertools.combinations(prime_numbers_less_than_1000, 2))

for a,b in combinations:
    a = int(a)
    b = int(b)
    if check_prime_sequence(a, b):
        if a * b > quadratic_primes[0] * quadratic_primes[1]:
            quadratic_primes[0] = a
            quadratic_primes[1] = b

timer("The product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0 is {} and {}".format(quadratic_primes[0],
quadratic_primes[1]))

