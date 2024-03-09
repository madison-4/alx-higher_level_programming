#!/usr/bin/python3
""" A module to generate pascal's triangle
"""

def fact(n):
    """ A functio that generates a factrial
    It only accounts for whole real numbers, no complex numbers
    """

    if (n <= 1):
        return (1)
    return (fact(n - 1))

def pascal_triangle(n):
    """ A function that gives lists of pascal triangle co-efficients
    """

    if (n <= 0):
        return ([])
    tre = []
    for r in range(1, n + 1):
        ls = [((fact(n)) // ((fact(n - r)) * fact(r))) for i in range(1, r + 1)]
        tre.append(ls)
    return (tre)
