import time
import math

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

# pos = 0 get square number, pos = 1 get cube number, pos = 2 get quad number
def get_val(n, pos):
    if n not in look_up:
        _sqn = n * n
        look_up[n] = [_sqn, _sqn * n, _sqn * _sqn]
    return look_up.get(n)[pos]

timer = timing()

limit =  50000000
primes = get_prime_numbers(int(math.sqrt(limit)))
look_up = {}
count = set() # to handle duplications

for x in primes:
    sq = get_val(x, 0)
    
    if sq > limit:
        break

    for y in primes:
        cb = get_val(y, 1)
        total_sq_cb = sq + cb

        if total_sq_cb > limit:
            break

        for z in primes:
            qd = get_val(z, 2)
            total = total_sq_cb + qd
            
            if total < limit:
                count.add(total)
            elif total > limit:
                break

timer("There are {} numbers below fifty million which can be expressed as the sum of a prime square, prime cube, and prime fourth power".format(len(count)))
