#!/usr/bin/python3
"""
module indentation
"""

def text_indentation(text):
    """function prints indented text"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i in [".", "?", ":"]:
            print(i)
            print()
        else:
            print(i, end="")
