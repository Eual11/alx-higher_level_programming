#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    wholematrix = []
    for i in range(len(matrix)):
        squared = []
        for j in matrix[i]:
            squared += j ** 2
        wholematrix += squared
    return wholematrix
