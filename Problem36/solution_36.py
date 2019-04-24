import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def isAPallindrome(input):
    if input == input[::-1]:
        return True
    return False

timer = timing()

limit = 1000000
numbers = list(range(1, limit))
palindromes = []

for number in numbers:
    if isAPallindrome(str(number)) and isAPallindrome("{0:b}".format(number)):
        	palindromes.append(number)

timer("The sum of all numbers, less than one million, which are palindromic in base 10 and base 2 are {}".format(sum(palindromes)))
