#!/usr/bin/python3
for x in range(90, 64, -1):
    if x % 2 != 0:
        alpha = x
    else:
        alpha = x + 32
    print("{:s}".format(chr(alpha)), end="")
