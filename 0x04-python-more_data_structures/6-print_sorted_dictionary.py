#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = dict(sorted(a_dictionary.items(), key=lambda x: x[0]))
    for items in a_dictionary.items():
        print(items[0]+":", items[1])