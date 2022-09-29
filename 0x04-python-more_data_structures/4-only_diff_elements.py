#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    out_set = set({})
    out_set = set_1.difference(set_2)
    out_set.update(set_2.difference(set_1))
    return out_set
