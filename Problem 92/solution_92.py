import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def squareAndAdd(x):
    total = 0
    temp_list = [int(x)]
    while True:
        total = 0
        for digit in x:
            total += squares.get(digit)
        if square_digit_chain.get(total):
            total = square_digit_chain.get(total)
            break
        elif total == 89 or total == 1:
            break
        temp_list.append(total)
        x = str(total)
    for number in temp_list:
        square_digit_chain[number] = total
    return total
    
timer = timing()
limit = 10 ** 7 
counter = 0
square_digit_chain = {}
squares = {'1':1, '2':4,'3':9,'4':16,'5':25,'6':36,'7':49,'8':64,'9':81,'0':0}

for i in range(1, limit):
    total = squareAndAdd(str(i))
    if total == 89:
        counter += 1

timer("There are {} starting numbers below ten million which will arrive at 89".format(counter))
