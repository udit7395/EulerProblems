import math 
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def is_divisible_by_x(arg, x):
    return (arg % x == 0)

timer = timing()
limit = 10000

proper_divisors_dict = {}

for a in range(2, limit):
    proper_divisors_list = [1]
    for b in range(2, a//2 + 1):
        if is_divisible_by_x(a, b):
            proper_divisors_list.append(b)
    proper_divisors_dict[a] = sum(proper_divisors_list)
    
amicable_numbers = []
for number, sum_of_divisors in proper_divisors_dict.items():
    if number != sum_of_divisors:
        if proper_divisors_dict.get(sum_of_divisors) == number:
            if sum_of_divisors not in amicable_numbers:
                amicable_numbers.append(number)
                amicable_numbers.append(sum_of_divisors)

timer("The sum of all the amicable numbers under 10000 is {}".format(sum(amicable_numbers)))
