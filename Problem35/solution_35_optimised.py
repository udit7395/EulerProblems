import math
import time
import itertools

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def rotate_and_check(input):
    inputLength = len(input)
    for index in range(0, inputLength):
        input = input[-1] + input[0:inputLength-1]	
        if input not in prime_numbers:
            return False
    return True

timer = timing()

n = 1000000
input_array = [1] * n
prime_numbers = []
circular_primes = []
goodNums = set(['1','3','7','9'])
good_filter = lambda x: not set(x).difference(goodNums)
p = 2

for index in range(2, int(math.sqrt(n)) + 1):
    if input_array[index] is 1:
        for temp in range(p*2, n, p):
            input_array[temp] = 0
    p = p + 1

for index in range(2, n):
    if input_array[index] is 1:
        prime_numbers.append(str(index))

prime_numbers = list(filter(good_filter, prime_numbers))

for prime_number in prime_numbers:
    if rotate_and_check(prime_number):
            circular_primes.append(prime_number) 

circular_primes.append(2)
circular_primes.append(5)     

timer("There are {} Circular primes below one million".format(len(circular_primes)))
