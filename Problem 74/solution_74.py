import time
import math
from collections import Counter

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def getFactorials():
    factorials = {}
    for i in range(10):
        factorials[str(i)] = math.factorial(i)
    return factorials

def check(n):
    temp = [n]
    length = 1
    while True:
        total = 0
        for digit in str(temp[-1]):
            total += factorials.get(digit)
        if total == temp[-1]:
            break
        elif total not in look_up:
            length += 1
            temp.append(total)
        else:
            length += look_up.get(total)
            break
    for index, val in enumerate(temp):
        look_up[val] = length - index
    return look_up.get(n)

timer = timing()

limit = 10 ** 6
count = 0
look_up = {169 : 3, 871 : 2, 872 : 2, 145: 1, 0: 1, 1 : 1, 2: 1}

factorials = getFactorials() 

for i in range(limit):
    if check(i) == 60:
        count += 1

timer("There are {} chains below one million, containing exactly sixty non-repeating terms".format(count))
