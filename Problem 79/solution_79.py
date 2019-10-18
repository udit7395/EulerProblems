import time
import string

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()

input_file = open('p079_keylog.txt', 'r').readlines()

secret_passcode = ""
passcode_info = {}

for line in input_file:
    x, y, z = int(line[0]), int(line[1]), int(line[2])

    temp = passcode_info.get(z)
    if temp:
        if x not in temp and z != x:
            temp.append(x)
        if y not in temp and z != y:
            temp.append(y)
    else:
        passcode_info[z] = [x, y]
    
    temp = passcode_info.get(y)
    if temp:
        if x not in temp and y != x:
            temp.append(x)
        passcode_info[y] = temp
    else:
        passcode_info[y] = [x]

    temp = passcode_info.get(x)
    if not temp:
        passcode_info[x] = []

for digit in sorted(passcode_info.items(), key = lambda x : len(x[1])):
    secret_passcode += str(digit[0])

timer("The shortest possible secret passcode of unknown length is {}".format(secret_passcode))
