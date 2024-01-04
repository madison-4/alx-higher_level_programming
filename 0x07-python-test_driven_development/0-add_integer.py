#!/usr/bin/python3
# a function to add two integers or floats

def add_integer(a, b=98):
    """A simple addition function
    It adds two integers and returns the results
    Some tests here
    # Test for function of addition
    # The tests should ensure that the inputs are correct and the output.
    # ideally they should ensure the function works as intended
    
    >>> add_integer(3, b)
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer
    >>> add_integer(a, 3)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    >>> add_integer({56, 67}, 67)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    >>> add_integer(56, {98, 76})
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer
    >>> add_integer('str', 'stry')
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    >>> add_integer([90, 89], 87)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    """
    
    try: a
    except: NameError
    raise TypeError("a must be an integer")
    try: b
    except: raise TypeError("b must be an integer")
    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    return (a + b)
