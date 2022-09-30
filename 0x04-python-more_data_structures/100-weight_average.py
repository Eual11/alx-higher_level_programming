from itertools import count


def weight_average(my_list=[]):
    if (not len(my_list)):
        return 0
    sum = 0
    weight = 0
    for value in my_list:
        sum += (value[0]*value[1])
        weight += value[1]
    return sum/weight
