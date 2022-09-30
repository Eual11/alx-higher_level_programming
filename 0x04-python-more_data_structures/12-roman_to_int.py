#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return 0
    va_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    int_value = 0
    for i in range(0, len(roman_string)):
        if (not va_dict.get(roman_string[i], 0)):
            return 0
        if (i < len(roman_string) - 1 and
           va_dict.get(roman_string[i]) < va_dict[roman_string[i+1]]):
            int_value -= va_dict[roman_string[i]]
        else:
            int_value += va_dict[roman_string[i]]
    return int(int_value)
