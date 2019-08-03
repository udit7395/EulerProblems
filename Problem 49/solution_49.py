import math
import itertools
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def get_prime_numbers(n, inStringFormat = False):
    p = 2
    input_array = [1] * n
    for index in range(2, int(math.sqrt(n)) + 1):
        if input_array[index] is 1:
            for temp in range(p*2, n, p):
                input_array[temp] = 0
        p = p + 1

    if inStringFormat:
        prime_numbers = list(str(index) for index in range(2, n) if input_array[index])
    else:
        prime_numbers = list(index for index in range(2, n) if input_array[index])

    return prime_numbers

def check_property(prime_number):
	permutation_prime_numbers = []
	for permutation in itertools.permutations(prime_number):
		permutation_prime_number = int(''.join(permutation))
		if permutation_prime_number in special_property:
			return None
		elif permutation_prime_number in prime_numbers and permutation_prime_number not in permutation_prime_numbers:
			permutation_prime_numbers.append(permutation_prime_number)

	for i in permutation_prime_numbers:
		for j in permutation_prime_numbers:
			if i > j:
				if i + i - j in permutation_prime_numbers:
					return [j, i, i + i - j]
	return None

timer = timing()
special_property = {}
prime_numbers = list(filter(lambda x: len(str(x)) == 4, get_prime_numbers(10000)))
output_string = ""
for prime_number in prime_numbers:
	permutation_prime_number = check_property(str(prime_number))
	if permutation_prime_number:
		special_property[prime_number] = permutation_prime_number

timer("The prime permutations which exhibit the following property (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another are {}".format(special_property))