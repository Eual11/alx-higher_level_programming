#!/usr/bin/python3
"""creating a class"""


class Square:
    """a method"""

    def __init__(self, size=0):
        """initialize a size"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """return square area"""
    def area(self):
        return self.__size * self.__size
