import time

def timing():
	start_time = time.time()
	return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()

limit = 10 ** 10
power = 7830457
ans = 1

for i in range(power):
    ans = 2 * ans
    if ans > limit:
        ans = int(str(ans)[-10:])

ans = ans * 28433 + 1
last_ten_digits = str(ans)[-10:]

timer("The last ten digits of the massive non-Mersenne prime which contains 2,357,207 digits: ((28433×(2^7830457)) + 1) is {}".format(last_ten_digits))