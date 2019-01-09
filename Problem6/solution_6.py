import math
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()

argument = 100
limit = argument
sum_of_the_squares = 0
squares_of_the_sum = (limit * (limit + 1))
for natural_number in range(1,limit):
    sum_of_the_squares = sum_of_the_squares + natural_number*natural_number

squares_of_the_sum = squares_of_the_sum * squares_of_the_sum

print("Sum of the squares  is %d" % sum_of_the_squares) 
print("Squares of the sum is %d" % squares_of_the_sum)

timer("Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {}".format(sum_of_the_squares - squares_of_the_sum))
