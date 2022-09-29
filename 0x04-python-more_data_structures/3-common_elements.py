#!/usr/bin/python3
def common_elements(set_1, set_2):
    out_set = set({})
    out_set = set_1.intersection(set_2)
    return out_set
