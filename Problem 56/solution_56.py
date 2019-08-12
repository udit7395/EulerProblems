import time
import math

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()
limit = 100
largest_sum = 0
for a in range(1, limit):
    for b in range(1, limit):
        total = sum(list(int(x) for x in str(a ** b))) 
        if total > largest_sum:
            largest_sum = total

timer("Considering natural numbers of the form, ab, where a, b < 100, the maximum digital sum is {}".format(largest_sum))
