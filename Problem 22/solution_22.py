import math 
import time
import string

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()

alphabetical_points = {}
final_sum = 0 

ascii_list = list(string.ascii_uppercase)

for index in range(0,26):
    alphabetical_points[ascii_list[index]] = index + 1

file_input = open("/home/udit/git/EulerProblems/Problem22/names.txt", "r")

names = file_input.read().replace("\"","").split(",")
names.sort()

for index in range(1, len(names) + 1):
    aggregate = 0
    for character in names[index - 1]:
        aggregate += alphabetical_points.get(character)
    aggregate *= index
    final_sum += aggregate

timer("The total of all the name scores in the file is {}".format(final_sum))
