#!/usr/bin/python3
def square_matrix_simple(matrix=[]) -> list:
    """squares matric"""

    outlist = []

    for list in matrix:
        temp = [value**2 for value in list]
        outlist.append(temp)
    return outlist

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)