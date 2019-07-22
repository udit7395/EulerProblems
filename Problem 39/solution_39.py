import time
import itertools

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))
 
timer = timing()
limit = 501
perimeters_dict = {}
largest = 0
perimeter = 0

for a in range(limit):
	for b in range(limit):
		for c in range(limit):
			if a < b and b < c and a ** 2 + b ** 2 == c ** 2:
				perimeter = a + b + c
				index = perimeters_dict.get(perimeter)
				if index:
					perimeters_dict[perimeter] = index + 1
				else:
					perimeters_dict[perimeter] = 1


for key,value in perimeters_dict.items():
	if value > largest:
		largest = value
		perimeter = key

timer("The value of p ≤ 1000 for which the number of solutions maximised is {}".format(perimeter))