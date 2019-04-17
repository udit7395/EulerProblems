import math
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()

limit = 1000000
factorion = []

for index in range(3, limit):
	aggregate = 0
	for number in str(index):
		aggregate += math.factorial(int(number))
	if aggregate == index:
		factorion.append(index)

timer("The sum of all numbers which are equal to the sum of the factorial of their digits under {} is {}".format(limit,sum(factorion)))
