import time
import itertools
import fractions

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()

start = 10
limit = 100
lcm = 1
numbers = list(number for number in range(start, limit) if not number % 10 == 0)
non_trivial_fractions = []

def check_if_cancelling_fraction(numerator, denominator):
    if numerator % 10 == denominator // 10:
        numerator_tenths_place = numerator // 10
        denominator_units_place = denominator % 10
        if numerator / denominator == numerator_tenths_place / denominator_units_place:
            return True
    else:
        numerator_units_place = numerator % 10
        denominator_tenths_place = denominator // 10
        if  numerator / denominator == numerator_units_place / denominator_tenths_place:
            return True
    return False


for combination in itertools.combinations(numbers, 2):
    numerator = combination[0]
    denominator = combination[1]
    if numerator % 10 == denominator // 10 or numerator // 10 == denominator % 10:
        if check_if_cancelling_fraction(numerator, denominator):
            non_trivial_fractions.append(str(numerator) + "/" + str(denominator))
            lcm = lcm * numerator / denominator

lcm = str(fractions.Fraction(str(lcm))).split("/")[1]

timer("The 4 non trivial fractions are as follows {} \n\
The value of the denominator for the product of these four fractions is given in its lowest common terms is {}".format(non_trivial_fractions, lcm))