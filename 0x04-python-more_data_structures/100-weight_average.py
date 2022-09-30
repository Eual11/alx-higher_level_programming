#!/usr/bin/python3


def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    sum = 0
    weight = 0
    for value in my_list:
        if (len(tuple(value)) != 2):
            return 0
        sum += (value[0]*value[1])
        weight += value[i]
    return sum/weight
