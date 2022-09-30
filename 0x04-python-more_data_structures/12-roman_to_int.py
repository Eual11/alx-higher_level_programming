#!/usr/bin/python3
import string


def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return 0
    va_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    int_value = 0
    for char in roman_string:
        if (not va_dict.get(char, 0)):
            return 0
        int_value += va_dict[char]
    return int(int_value)
