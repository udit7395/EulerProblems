import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()
spiral_size = 1001
limit = spiral_size // 2 + 1
diagonal_total = 1

"""
The top right diagonal sequence [9, 25, 49, 81,...] are squares of odd numbers (2n + 1) ^ 2 => X
The top left diagonal sequence [7, 21, 43, 73,...] can then be generated by subracting 2n from above sequence => X - 2n
The bottom left diagonal sequence [5, 17, 37, 65,...] can then be generated by subracting 2n from the above sequence []=> X - 4n
The bottom right diagonal sequence [3, 13, 31, 57,...] can then be generated by subracting 2n from above sequence => X - 6n

The sum of the diagonal is the addition of the above, i.e, 4 * ((2 * n + 1) ** 2) - 12 * n 
"""

for n in range(1, limit):
	diagonal_total += 4 * ((2 * n + 1) ** 2) - 12 * n 

timer("The sum of the numbers on the diagonals in a 1001 by 1001 spiral formed is {}".format(diagonal_total))
