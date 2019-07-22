import math
import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def print_matrix(arg):
    output = ""
    for i in range(len(arg)):
        for j in range(len(arg[i])):
            output += str('{:2d}').format(arg[i][j]) + " "
        output += "\n"
    print(output)

def some_function(horizontal_product, vertical_product, diagonal_product_1, diagonal_product_2):
    if (horizontal_product > vertical_product and horizontal_product > diagonal_product_1 and horizontal_product > diagonal_product_2):
        # print("horizontal_product")
        return horizontal_product
    elif (vertical_product > diagonal_product_1 and vertical_product > diagonal_product_2):
        # print("vertical_product")
        return vertical_product
    elif (diagonal_product_1 > diagonal_product_2):
        # print("diagonal_product_1")
        return diagonal_product_1
    else:
        # print("diagonal_product_2")
        return diagonal_product_2

def calulate_product(arg, index_row, index_col):
    if(index_col + 3 < col_length):
        horizontal_product = arg[index_row][index_col] * \
            arg[index_row][index_col + 1] * \
            arg[index_row][index_col + 2] * arg[index_row][index_col + 3]
    else:
        horizontal_product = 0

    if(index_row + 3 < row_length):
        vertical_product = arg[index_row][index_col] * \
            arg[index_row + 1][index_col] * \
            arg[index_row + 2][index_col] * arg[index_row + 3][index_col]
    else:
        vertical_product = 0

    if horizontal_product != 0 and vertical_product != 0:
        diagonal_product_1 = arg[index_row][index_col] * \
            arg[index_row + 1][index_col + 1] * \
            arg[index_row + 2][index_col + 2] * \
            arg[index_row + 3][index_col + 3]

        diagonal_product_2 = arg[index_row][index_col] * \
            arg[index_row + 1][index_col - 1] * \
            arg[index_row + 2][index_col - 2] * \
            arg[index_row + 3][index_col - 3]
    else:
        diagonal_product_1 = 0
        diagonal_product_2 = 0

    return some_function(horizontal_product, vertical_product, diagonal_product_1, diagonal_product_2)


timer = timing()

input_matrix = [[ 8,  2, 22, 97, 38, 15,  0, 40,  0, 75,  4,  5,  7, 78, 52, 12, 50, 77, 91,  8],
                [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48,  4, 56, 62,  0],
                [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30,  3, 49, 13, 36, 65],
                [52, 70, 95, 23,  4, 60, 11, 42, 69, 24, 68, 56,  1, 32, 56, 71, 37,  2, 36, 91],
                [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
                [24, 47, 32, 60, 99,  3, 45,  2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
                [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
                [67, 26, 20, 68,  2, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21],
                [24, 55, 58,  5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
                [21, 36, 23,  9, 75,  0, 76, 44, 20, 45, 35, 14,  0, 61, 33, 97, 34, 31, 33, 95],
                [78, 17, 53, 28, 22, 75, 31, 67, 15, 94,  3, 80,  4, 62, 16, 14,  9, 53, 56, 92],
                [16, 39,  5, 42, 96, 35, 31, 47, 55, 58, 88, 24,  0, 17, 54, 24, 36, 29, 85, 57],
                [86, 56,  0, 48, 35, 71, 89,  7,  5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
                [19, 80, 81, 68,  5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,  4, 89, 55, 40],
                [ 4, 52,  8, 83, 97, 35, 99, 16,  7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
                [88, 36, 68, 87, 57, 62, 20, 72,  3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
                [ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36],
                [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74,  4, 36, 16],
                [20, 73, 35, 29, 78, 31, 90,  1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,  5, 54],
                [ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52,  1, 89, 19, 67, 48]]

# test_matrix = [[8, 2, 22, 97, 38, 15],
#                 [49, 49, 99, 40, 17, 81],
#                 [81, 49, 31, 73, 55, 79],
#                 [52, 70, 95, 23,  4, 60],
#                 [22, 31, 16, 71, 51,  0]]

# test_matrix = [[29, 2, 3, 40, 5],
#                 [28, 7, 35, 9, 10],
#                 [21, 22, 23, 24, 25],
#                 [99, 12, 13, 14, 15],
#                 [16, 17, 18, 19, 20]]

# input_matrix = test_matrix

largest_product = 0
row_length = len(input_matrix)
col_length = len(input_matrix[1])

print("%d row %d col" % (row_length, col_length))
print_matrix(input_matrix)

for i in range(0, row_length):
    for j in range(0, col_length):
        if input_matrix[i][j] != 0:
            product = calulate_product(input_matrix, i, j)
            # print(product)
            if(product >= largest_product):
                largest_product = product
                # print("%d row %d col %d value %d value  %d largest product" % 
                    #   (i, j, input_matrix[i][j], input_matrix[i+1][j+1], largest_product))

# print(largest_product)
timer("The greatest product of four adjacent numbers in the same direction\n (up, down, left, right, or diagonally) in the 20×20 grid is {}".format(largest_product))
