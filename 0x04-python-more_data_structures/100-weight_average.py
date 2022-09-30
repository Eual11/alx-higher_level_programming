#!/usr/bin/python3


def weight_average(my_list=[]):
    if (not my_list):
        return 0
    if (not isinstance(my_list, list)):
        return 0
    sum = 0
    weight = 0
    for value in my_list:
        sum += (value[0]*value[1])
        weight += value[i]
    return sum/weight
