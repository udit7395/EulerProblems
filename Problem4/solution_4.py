import math
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def is_palindrome(x):
    return str(x) == str(x)[::-1] 

timer = timing()

upper_limit = 999
lower_limit = 100
largest_product = 0
number_1 = 0
number_2 = 0
for i in range(upper_limit, lower_limit, -1):
    for j in range(upper_limit, lower_limit, -1):
        product = i*j
        if (is_palindrome(product)) and largest_product <  product:
            print("Number_1 = %d, Number_2 = %d" % (i,j))
            print("Product = %d\n" % (product))
            largest_product = product
            number_1 = i
            number_2 = j
            break

timer("The largest palindrome made from the product of two 3-digit numbers ({},{}) is {}".format(number_1, number_2, largest_product))
