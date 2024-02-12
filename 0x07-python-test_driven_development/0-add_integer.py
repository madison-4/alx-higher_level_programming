#!/usr/bin/python3
""" This module adds two integers and tests my testing skills
"""


def add_integer(a, b=98):
    """A simple addition function
    It adds two integers and returns the results
    Some tests here
    # Test for function of addition
    # The tests should ensure that the inputs are correct and the output.
    # ideally they should ensure the function works as intended

    TypeError: a must be an integer
    """

    try:
        a
    except NameError:
        raise NameError('You have to define a')
    else:
        pass
    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    return (a + b)
