#!/usr/bin/python3
# A function that computes the value of a square matric of all ints
# the function prints a sqaure matrix
def square_matrix_simple(matrix=[]):
    return ([[elem**2 for elem in matrix[i]] for i in range(len(matrix))])
