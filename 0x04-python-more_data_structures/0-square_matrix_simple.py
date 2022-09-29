#!/usr/bin/python3
def square_matrix_simple(matrix=[]) -> list:
    """squares matric"""
    temp_list = matrix[:]
    outlist = []

    for list in temp_list:
        temp = [value**2 for value in list]
        outlist.append(temp)
    return outlist
