import math
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

timer = timing()

limit = 1000000
prime_numbers = get_prime_numbers(limit)
set_prime_numbers = set(prime_numbers)
consecutive_prime_sequence_length = 0
largest_sum_prime = 0
start_index = 1

prime_sum = sum(prime_numbers)
end_index = len(prime_numbers)

while prime_sum >= limit:
    end_index -= 1
    prime_sum -= prime_numbers[end_index]

for i in range(end_index + 1):
    for j in range(start_index, end_index + 1):
        prime_sum = sum(prime_numbers[i:j])
        if prime_sum in set_prime_numbers:
            if len(prime_numbers[i:j]) >= consecutive_prime_sequence_length:
                consecutive_prime_sequence_length = len(prime_numbers[i:j])
                largest_sum_prime = prime_sum
                start_index = j
    
timer("The prime number, below one-million, which can be written as the sum of the most consecutive primes is {}".format(largest_sum_prime))