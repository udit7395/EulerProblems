import math 
import time
import decimal 

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def getDecimalFractionForN(n):
    with decimal.localcontext() as ctx:
        ctx.prec = 10000
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

for number in range(2, limit):
    decimals = getDecimalFractionForN(number)
    if len(decimals) >= 900:
        rlength, rterm = getRecurringLengthAndTerm(decimals)
        if rlength >= recurring_length:  
            recurring_length = rlength
            longest_recurring_cycle_number = number
            recurring_term = rterm

timer("The value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part is {}".format(longest_recurring_cycle_number))
