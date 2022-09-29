#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for items in a_dictionary.items():
        new_dict[items[0]] = items[1]*2
    return new_dict
