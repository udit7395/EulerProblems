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

def is_permutation(x, y):
    str_x = str(x)
    str_y = str(y)
    if sorted(str_x) == sorted(str_y):
        return True
    else:
        return False

timer = timing()

prime_limit = 10 ** 4 + 10
n_limit = 10 ** 7

primes = get_prime_numbers(prime_limit)
len_primes = len(primes)

min_totient = n_limit
N = 0

for index_i, i in enumerate(primes):
    for index_j in range(index_i, len_primes):
        j = primes[index_j]
        n = i * j
        if n < n_limit:
            phi = (i - 1) * (j - 1)
            totient = n / phi
            if totient < min_totient and is_permutation(n, phi):
                min_totient = totient
                N = n
        else:
            break

timer("The value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum is {}".format(N))
