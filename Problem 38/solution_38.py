import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def isAPandigital(input):
    for number in panDigital_number_list:
        if input.count(number) != 1:
            return False
    return True

timer = timing()
limit = 10000
panDigital_number_list = list(str(number) for number in range(1, 10))
largest_pandigital_number = 0

for i in range(limit):
    break_loop = False
    j = 1
    output = ""
    while not break_loop:
        output += str(i * j)
        length_of_output_string = len(output)
        if length_of_output_string == 9:
            if isAPandigital(output):
                if int(output) > largest_pandigital_number:
                    largest_pandigital_number = int(output)
                    break
        elif length_of_output_string >= 9:
            break_loop = True
            break
        j += 1

timer("The largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1 is {}".format(largest_pandigital_number))
