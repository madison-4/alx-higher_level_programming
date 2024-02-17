#!/usr/bin/python3
""" This module defines a square printing function
"""


def print_square(size):
    """ It prints a square of width size
    Of course size must be an int >=0
    """

    if (type(size) is not int):
        raise TypeError('size must be an integer')
    if (size < 0):
        raise ValueError('size must be >= 0')
    for height in range(size):
        for row in range(size):
            print('#', end='')
        print()
    print
