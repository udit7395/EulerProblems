import time
import itertools

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()
limit = 100000
triangle = []
pentagonal = []
hexagonal = []

for index in range(2, limit):
	triangle.append(index * (index + 1) // 2)
	pentagonal.append(index * (3 * index - 1) // 2)
	hexagonal.append(index * (2 * index - 1))

timer("The next triangle number after 40755 that is also pentagonal and hexagonal is {}".format(list(set(triangle) & set(pentagonal) & set(hexagonal))[1]))

