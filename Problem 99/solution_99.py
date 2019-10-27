import time
import math

def timing():
	start_time = time.time()
	return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()

lines = open('p099_base_exp.txt', 'r').readlines()
 
largest = 0
line_number = 0

for index, line in enumerate(lines):
    base, exponent = line.rstrip().split(',')
    output = int(exponent) * math.log10(int(base))
    if output > largest:
        largest = output
        line_number = index + 1
       
timer("The line number that has the greatest numerical value[base/exponent pair] is {}".format(line_number))
