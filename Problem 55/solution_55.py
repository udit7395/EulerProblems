import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def isPallindromic(x):
    if x != x[::-1]:
        return False
    return True

def isLyrchelNumber(x):
    j = 1
    while j != 50:
        total = x + int(str(x)[::-1])
        if isPallindromic(str(total)):
            return False
        else:
            x = total
            j += 1
    return True

timer = timing()
limit = 10000
lychrel_number_counter = 0

for i in range(10, limit + 1):
    if isLyrchelNumber(i):
        lychrel_number_counter += 1

timer("There are {} Lychrel numbers below ten-thousand".format(lychrel_number_counter))
