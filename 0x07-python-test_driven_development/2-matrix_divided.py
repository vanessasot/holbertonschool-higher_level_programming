#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Instructions to realize the division"""
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    if div == 0:
        raise ZeroDivisionError("divisiom by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be number")
    for i, row in enumerate(matrix):
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if not all([isinstance(k, (int, float)) for k in row]):
            raise TypeError("matrix must be a matrix (list of lists)"
                           "of integers/floats")
    return [[round(i/div, 2) for i in row] for row in matrix]
