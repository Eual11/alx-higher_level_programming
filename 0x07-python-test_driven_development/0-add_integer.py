#!/usr/bin/python3
"""
"0-add-integer" module.
"""

def add_integer(a, b=98):
    """Returns sum of a and b"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a + b))
