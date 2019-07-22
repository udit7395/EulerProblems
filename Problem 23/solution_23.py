import math 
import time
import itertools

def timing():
	start_time = time.time()
	return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def is_divisible_by_x(arg, x):
	return (arg % x == 0)

timer = timing()
limit = 28123

not_sum_of_abundant_numbers = list(range(1, limit))
abundant_numbers = []
result = []

for a in range(2, limit):
	proper_divisors_list = [1]
	for b in range(2, int(math.sqrt(a)) + 1):
		if is_divisible_by_x(a, b):
			proper_divisors_list.append(b)
			if(a//b != b):
				proper_divisors_list.append(a//b)
	aggregate = sum(proper_divisors_list)
	if aggregate > a and aggregate <= limit:
		abundant_numbers.append(a)

for i in itertools.combinations_with_replacement(abundant_numbers, 2):
	result.append(sum(i))

#Remove the sums of two abundant numbers from the list
not_sum_of_abundant_numbers = list(set(not_sum_of_abundant_numbers) - set(result))
			 
timer("The sum of all the positive integers which cannot be written as the sum of two abundant numbers is {}".format(sum(not_sum_of_abundant_numbers)))

