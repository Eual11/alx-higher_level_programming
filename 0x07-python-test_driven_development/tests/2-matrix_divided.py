#!/usr/bin/python3
"""
matrix module
"""


def matrix_divided(matrix, div):
    """return a list divided by div"""
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    for i in range(len(matrix)):
        if len(matrix[i-1]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in range(len(i)):
            if type(i[j]) is not int and type(i[j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(i / div, 2) for i in lis] for lis in matrix]
