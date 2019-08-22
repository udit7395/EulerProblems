import time

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

timer = timing()
number_count = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

def getPositionOfNumbers(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    return pos_nums

def getCount(number):
    units = ""
    tens = ""
    hundreds = ""
    thousands = ""
    posNums = getPositionOfNumbers(number)
    len_posNums = len(posNums)
    if len_posNums == 4:
        if posNums[2] == 0 and posNums[1] == 0 and posNums[0] == 0: 
            thousands = number_count.get(posNums[3]) + " thousand "     
        else:
            thousands = number_count.get(posNums[3]) + " thousand and "
    if len_posNums >= 3 and posNums[2] > 0:
        if posNums[1] == 0 and posNums[0] == 0:
            hundreds = number_count.get(posNums[2]) + " hundred "
        else:
            hundreds = number_count.get(posNums[2]) + " hundred and "
    if posNums[1] == 1 and posNums[0] > 0:
        tens = number_count.get(int(str(posNums[1]) + str(posNums[0])))
    else:
        if len_posNums >= 1 and posNums[1] > 0:
            tens = number_count.get(posNums[1] * 10) + " "
        if len_posNums >= 0 and posNums[0] > 0:
            units = (number_count.get(posNums[0]))
    output = thousands + hundreds + tens + units
    return len(output.replace(" ", "")), output

timer = timing()
count = 0
limit = 1000
output = ""

for index in range(1, limit + 1):
    if number_count.get(index):
        count += len(number_count.get(index))
        output += str(index) + " + "
    else:
        x, y = getCount(index)
        number_count[index] = y
        count += x
        output += str(index) + " + "

timer("{} letters would be used, if all the numbers from 1 to 1000 (one thousand) inclusive were written out in words".format(count))
