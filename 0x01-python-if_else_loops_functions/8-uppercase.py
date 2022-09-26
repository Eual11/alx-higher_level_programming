#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) < 123 and ord(i) >= 97:
            char = chr(ord(i) - 32)
        else:
            char = i
        print("{:s}".format(char), end="")
    print('')
