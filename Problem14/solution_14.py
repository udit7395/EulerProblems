import math 
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def is_n_even(n):
    return n % 2 == 0

timer = timing()
limit = 3
final_limit = 1000000
biggest_sequence_length = 0
biggest_sequence_starter = 0
collatz_sequence = {2:2}

def get_sequnce_for_n(n):
    seq_list = [n]
    while n != 2:
        if n not in collatz_sequence:
            if is_n_even(n):
                n = int(n/2) 
            else:
                n = (3 * n  + 1)
            seq_list.append(n)
        else:
            return len(seq_list) + collatz_sequence.get(n)
    return len(seq_list) + 2

while(limit < final_limit):
    collatz_sequence[limit] = get_sequnce_for_n(limit)
    limit += 1

for number, seq_len in collatz_sequence.items():
    if seq_len > biggest_sequence_length:
        biggest_sequence_length = seq_len
        biggest_sequence_starter = number

timer("The starting number, under one million, which produces the longest chain is {}".format(biggest_sequence_starter))