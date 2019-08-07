import time
import itertools
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
limit = 10000
index = 0
odd_composites = []
numbers = list(x for x in range(1, limit))
prime_numbers = get_prime_numbers(limit) 
odd_numbers = list(set(list(filter(lambda x: x % 2 != 0, numbers))).difference(set(prime_numbers)))
odd_numbers.sort()

for i in range(1, len(odd_numbers)):
    odd_number = odd_numbers[i]
    for prime_number in prime_numbers:
        j = 1
        while True:
            aggregate = prime_number + 2 * (j ** 2)
            if odd_number == aggregate:
                odd_composites.append(odd_number)
                break
            elif aggregate > odd_number:
                break
            if j >= 50:
                break
            j += 1
        if odd_number in odd_composites or prime_number > odd_number:
            break
    if odd_number not in odd_composites:
        index = i 
        break

timer("The smallest odd composite that cannot be written as the sum of a prime and twice a square is {}".format(odd_numbers[i]))
