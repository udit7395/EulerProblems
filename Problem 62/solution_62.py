import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def getNumberCount(n):
    number_count = {}
    for i in n:
        number_count[i] = n.count(i)
    return number_count

def isCountSame(nc, x):
    for number, count in nc.items():
        if x.count(number) != count:
            return False
    return True

def getCubePermutations(index, n):
    nc_dict = getNumberCount(n)
    len_n = len(n)
    filter_valid_cubes = lambda x: len(x) == len_n and not set(x).difference(n) and isCountSame(nc_dict, x)
    perm_cubes = list(filter(filter_valid_cubes, cubes_list[index:]))
    return perm_cubes 

timer = timing()
limit = 10000
cubes_list = [str(x ** 3) for x in range(1, limit)]
permutations_count = 5 

for index, cube in enumerate(cubes_list):
    cube_permutations = getCubePermutations(index, cube)
    if len(cube_permutations) == permutations_count: 
        timer("The smallest cube for which exactly five permutations of its digits are cube is {}".format(index + 1))
        break
