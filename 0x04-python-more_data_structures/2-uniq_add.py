#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp_list = my_list[:]
    out_set = {}
    out_set = set(out_set)
    for val in temp_list:
        out_set.add(val)
    return sum(out_set)
