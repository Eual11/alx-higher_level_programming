#!/usr/bin/python3
"""Defining a class Rectangle"""


class Rectangle:
    """
    attributes:
        width, height
    methods:
        getter and setter methods for height and width
    """
    def __init__(self, width=0, height=0):
        """inistantiate width and height"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter method to return width instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method to set width to value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method to return height instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method to set height to value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
