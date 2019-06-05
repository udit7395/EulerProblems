import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def isAPandigital(input):
    if len(input) != len(panDigital_number_list):
        return False
    for number in panDigital_number_list:
        if number not in input and input.count(number) != 1:
            return False
    return True

timer = timing()

panDigital_number_list = list(str(number) for number in range(1, 10))
panDigital_products = []

for index1 in range(0, 500):
	for index2 in range(0, 2000):
		output = index1 * index2
		output_string = str(index1) + str(index2) + str(output)
		if isAPandigital(output_string):
			panDigital_products.append(output)

timer("The sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital is {}".format(sum(set(panDigital_products))))