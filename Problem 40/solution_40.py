import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))
 
timer = timing()
product = 1
limit = 1000000
power_limit = 6
irrational_decimal_fraction = "0."
base_lenght = len(irrational_decimal_fraction)

for index in range(limit + 1):
    irrational_decimal_fraction += str(index)

# product = int(irrational_decimal_fraction[base_lenght + 1]) * \
# int(irrational_decimal_fraction[base_lenght + 10]) * \
# int(irrational_decimal_fraction[base_lenght + 100]) * \
# int(irrational_decimal_fraction[base_lenght + 1000]) * \
# int(irrational_decimal_fraction[base_lenght + 10000]) * \
# int(irrational_decimal_fraction[base_lenght + 100000]) * \
# int(irrational_decimal_fraction[base_lenght + 1000000]) 

product = int(irrational_decimal_fraction[base_lenght + 1])

for index in range(power_limit):
    product *= int(irrational_decimal_fraction[base_lenght + 10 ** index])
    
timer("If dn represents the nth digit of the fractional part, then the value of the following expression d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000 is {}".format(product))