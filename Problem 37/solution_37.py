import math
import time
import itertools

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def rotate_and_check(input, removeFromSide):
    inputLength = len(input)
    for index in range(0, inputLength - 1):
        if removeFromSide == 'right':
            input = input[0:len(input) - 1]
        elif removeFromSide == 'left':
            input = input[1:]  
        if input not in prime_numbers:
            return False
    return True

timer = timing()

n = 1000000
# n = 1000
input_array = [1] * n
prime_numbers = []
truncatable_primes = []
goodNums = set(['1','2','3','5','7','9'])
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
    if rotate_and_check(prime_number, 'left') and rotate_and_check(prime_number, 'right'):
        if int(prime_number) > 10:
            truncatable_primes.append(int(prime_number)) 

timer("The sum of the only eleven primes that are both truncatable from left to right and right to left is {}".format(sum(truncatable_primes)))
