#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    for i in range(len(a)):
        if len(a) < 2:
            a.append(0)
    for i in range(len(b)):
        if len(b) < 2:
            b.append(0)
    if len(a) == 0:
        a = [0, 0]
    elif len(b) == 0:
        b = [0, 0]
    Sum = (a[0] + b[0], a[1] + b[1])
    totalSum = tuple(Sum)
    return totalSum
