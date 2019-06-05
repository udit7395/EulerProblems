import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()
limit = 1000
input_argument = 10
aggregate = 0

for index in range(1, limit + 1):
	aggregate += index ** index

digits = str(aggregate)

timer("The last {} digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000 are {}".format(input_argument, digits[-input_argument:]))

