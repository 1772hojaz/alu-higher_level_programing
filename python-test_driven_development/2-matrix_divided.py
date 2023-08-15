#!/usr/bin/python3
"""must be a list of integers or floats, otherwise"""


def matrix_divided(matrix, div):
    if matrix != float and matrix != int :
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each roe of the matrix must have the same size")
        if div != flaot and div != int:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        new_matrix = []
        for row in matrix:
            divide_elements = [round(element / div, 2) for element in row]
            return new_matrix
