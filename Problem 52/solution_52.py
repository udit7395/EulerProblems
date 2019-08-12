import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def checkSameDigits(x, n):
    if len(x) != len(n):
        return False
    for digit in n:
        if not (x.count(digit) == 1 and n.count(digit) == 1):
            return False
    return True

def checkPermutedMultiples(x):
    for i in range(2, 6 + 1):
        if not checkSameDigits(str(x), str(x * i)):
            return False
    return True

timer = timing()
limit = 1000000

for i in range(1, limit):
    if checkPermutedMultiples(i):
        timer("The smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits is {}".format(i))
        break
