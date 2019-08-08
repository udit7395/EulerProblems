import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()
ways_to_make_two_euros = 8

for a in range(1):
    for b in range(2):
        for c in range(4):
            for d in range(10):
                for e in range(20):
                    for f in range(40):
                        for g in range(100):
                            for h in range(200):
                                total = a * 200 + b * 100 + c * 50 + d * 20 + e * 10 + f * 5 + g * 2 + h * 1
                                if total == 200:
                                    ways_to_make_two_euros += 1
                                elif total > 200:
                                    break
                                if b == 1 and c == 2:
                                    break
                            if b == 1 and c == 2:
                                break
                        if b == 1 and c == 2:
                            break
                    if b == 1 and c == 2:
                        break
                if b == 1 and c == 2: 
                    break
            if b == 1 and c == 2:
                break
        if b == 1 and c == 2:
            break
                                
                                
timer("There are {} different ways that can make £2 by using eight coins [1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)]".format(ways_to_make_two_euros))
