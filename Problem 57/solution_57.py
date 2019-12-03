import time
import fractions
from decimal import Decimal

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()
limit = 1000
numerator = 3
denominator = 2
counter = 0

for i in range(1, limit):
    temp = denominator + numerator 
    numerator = denominator + temp
    denominator = temp
    if len(str(numerator)) > len(str(denominator)):
        counter = counter + 1

timer("In the first one-thousand expansions, there are {} fractions which contain a numerator with more digits than the denominator".format(counter))
