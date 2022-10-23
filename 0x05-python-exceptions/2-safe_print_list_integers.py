#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    plist = 0
    while True:
        try:
            if count < x:
                print("{:d}".format(my_list[count]), end="")
                count += 1
                plist += 1
            else:
                print()
                return plist
        except (TypeError, ValueError):
            count += 1
