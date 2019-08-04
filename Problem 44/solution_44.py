import itertools
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def calculatePentagonalNumbers(limit):
    pentagonal_numbers = []
    for n in range(1, limit):
        pentagonal_numbers.append((n * (3 * n - 1)) // 2)
    return pentagonal_numbers

def sumIsPentagonal(i, j):
    return pentagonal_numbers[i] + pentagonal_numbers[j] in set_pentagonal_number

def differenceIsPentagonal(i, j):
    return pentagonal_numbers[j] - pentagonal_numbers[i] in set_pentagonal_number

timer = timing()
limit = 3000
start_index = 0
end_index = 0

pentagonal_numbers = calculatePentagonalNumbers(limit)
set_pentagonal_number = set(pentagonal_numbers)

for i in range(len(pentagonal_numbers)):
    for j in range(end_index, len(pentagonal_numbers)):
        if sumIsPentagonal(i, j) and differenceIsPentagonal(i, j):
            start_index = i
            end_index = j

timer("The pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; The value of D is {}".format(abs(pentagonal_numbers[start_index] - pentagonal_numbers[end_index])))