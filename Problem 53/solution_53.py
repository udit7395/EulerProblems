import time
import math

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()
limit = 100
counter = 0
for n in range(1, limit + 1):
    for r in range(1, limit + 1):
        if n >= r:
            combinations = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
            if combinations > 1000000:
                counter += 1
        else:
            break

timer("There are {} value of nCr for 1≤n≤100, which are greater than one-million, not necessarily distinct".format(counter))
