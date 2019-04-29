import time
import itertools

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def is_divisible_by_x(arg, x):
    return (arg % x == 0)

timer = timing()
permutations = list(map("".join, itertools.permutations('1234567890')))
aggregate = 0

for number in permutations:
	if is_divisible_by_x(int(number[7:10]), 17) and is_divisible_by_x(int(number[6:9]), 13) and is_divisible_by_x(int(number[5:8]), 11) and is_divisible_by_x(int(number[4:7]), 7) and is_divisible_by_x(int(number[3:6]), 5) and is_divisible_by_x(int(number[2:5]), 3) and is_divisible_by_x(int(number[1:4]), 2):
		aggregate += int(number)

timer("The sum of all 0 to 9 pandigital numbers with this property are {}".format(aggregate))

