#!/usr/bin/python3
# A function that computes the value of a square matric of all ints
# the function prints a sqaure matrix
def square_matrix_simple(matrix=[]):
    ret = []
    for row in matrix:
        col = list(map(lambda x: x**2, row))
        ret.append(col)
    return (ret)
