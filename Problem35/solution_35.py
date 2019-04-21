import math
import time
import itertools

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def rotate_all_and_check(input):
    inputLength = len(input)
    input = input[-1] + input[0:inputLength-1]   
    for index in range(0, inputLength - 1):
        input = input[-1] + input[0:inputLength-1]	
        if input not in prime_numbers:
            return False
    return True

def rotate_once_and_check(input):
    return input[-1] + input[:-1] in prime_numbers

timer = timing()

n = 1000000
input_array = [1] * n
prime_numbers = []
right_rotated_once_prime_number = []
circular_primes = []
p = 2

for index in range(2, int(math.sqrt(n)) + 1):
    if input_array[index] is 1:
        for temp in range(p*2, n, p):
            input_array[temp] = 0
    p = p + 1

for index in range(2, n):
    if input_array[index] is 1:
        prime_number = str(index)
        prime_numbers.append(prime_number)
        right_rotated_once_prime_number.append(prime_number)

output = set(prime_numbers).intersection(set(right_rotated_once_prime_number))

for prime_number in output:
    if rotate_once_and_check(prime_number) and rotate_all_and_check(prime_number):
            circular_primes.append(prime_number)      

timer("There are {} Circular primes below one million".format(len(circular_primes)))
