import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()

summation = 0
limit = 4000000  
div_2 = 2

fibonnaci_number = [1, 2]

def is_divisible_by_x(arg, x):
    return (arg % x == 0)

def fibonnaci_series_till_x(x):
    start_num = 1
    last_num = 2
    for number in range(x):
        temp = start_num + last_num
        if temp > limit :
            break
        fibonnaci_number.append(temp)
        start_num = last_num
        last_num = temp

fibonnaci_series_till_x(limit)

for fibonnaci_num in fibonnaci_number:
    if is_divisible_by_x(fibonnaci_num, div_2):
        summation = summation + fibonnaci_num

timer("Sum of the even-valued terms in the Fibonacci sequence whose values do not exceed {} million is {}".format(limit, summation))
