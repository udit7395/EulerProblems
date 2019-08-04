import time
import math 
import itertools

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

def isAPrimeNumber(x):
    for index in range(int(math.sqrt(x))):
        if x % prime_numbers[index] == 0:
            return False
    return True

timer = timing()
limit = 1000000
prime_numbers = get_prime_numbers(limit)
largest_pandigital_prime = 0
pandigital_number = "123456789"
pandigital_number_length = 9

while pandigital_number_length!= 0:
    perumutations = list(map("".join, itertools.permutations(pandigital_number[:pandigital_number_length])))
    perumutations.sort()
    index = len(perumutations) - 1
    while index != 0:
        if isAPrimeNumber(int(perumutations[index])):
            largest_pandigital_prime = perumutations[index]
            break
        index -= 1
    if largest_pandigital_prime != 0:
        break
    pandigital_number_length -= 1

timer("The largest n-digit pandigital prime that exists is {}".format(largest_pandigital_prime))