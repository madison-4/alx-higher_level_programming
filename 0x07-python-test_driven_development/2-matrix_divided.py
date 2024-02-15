#!/usr/bin/python3
""" This module seesk to divvide a matrix then return the divide matrix
    The matrix should be of rows of equal size
    ::
    It simply defines a function
"""


def matrix_divided(matrix, div):
    """This is teh function to divide a mtraix
    """


    if (type(matrix) is not list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if (type(matrix[0]) is not list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    length = len(matrix[0])
    for i in matrix:
        if (type(i) is not list):
            raise TypeError('matrix must be a maatrix (list of lists) of integers/floats')
        if (len(i) != length):
            raise TypeError('Each row of the matrix must have the same size')
        for r in i:
            if (type(r) not in [int, float]):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if (type(div) not in [int, float]):
        raise TypeError('div must be a number')
    if (div == 0):
        raise ZeroDivisionError('divisin by zero')
    ans = []
    for row in matrix:
        rows = []
        for elem in row:
            elem = elem / div
            elem = round(elem, 2)
            rows.append(elem)
        ans.append(rows)
    return (ans)
