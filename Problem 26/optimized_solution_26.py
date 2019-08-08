import math 
import time
import decimal 

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

def getDecimalFractionForN(n):
    with decimal.localcontext() as ctx:
        ctx.prec = 2000
        return str(1 / (decimal.Decimal(n)))[2:]

def getRecurringLengthAndTerm(n):
    len_n = len(n)
    for i in range(len_n):
        for j in range(i + 1, len_n):
            rterm = n[i:j]
            output = n.split(rterm)
            len_output = len(output)
            if output[len_output - 2] == "" and len(output[len_output - 1]) > 0:
                return abs(i - j), rterm
    return 0

timer = timing()

limit = 1000
recurring_length = 0
longest_recurring_cycle_number = 0
recurring_term = ""
prime_numbers = get_prime_numbers(limit)

for prime_number in prime_numbers:
    decimals = getDecimalFractionForN(prime_number)
    if len(decimals) >= 900:
        rlength, rterm = getRecurringLengthAndTerm(decimals)
        if rlength >= recurring_length:  
            recurring_length = rlength
            longest_recurring_cycle_number = prime_number
            recurring_term = rterm

timer("The value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part is {}".format(longest_recurring_cycle_number))
