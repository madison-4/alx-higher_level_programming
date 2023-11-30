#!/usr/bin/python3
# A function that computes the value of a square matric of all ints
# the function prints a sqaure matrix
def square_matrix_simple(matrix=[]):
    res = []
    for row in matrix:
        newrow = [x**2 for x in row]
        res.append(newrow)
    return (res)
