import itertools
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()

limit = 10 
element = 1000000
index = 1
answer = ''

for permutation in itertools.permutations(range(limit), limit): 
    if index == element:
        for digit in permutation:
            answer += str(digit)
    index += 1

timer('The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 is {}'.format(answer))
