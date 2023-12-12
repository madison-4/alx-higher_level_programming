#!/usr/bin/python3
"""xDefine a square class that takes a square
The sqaure class is empty
"""


class Square:
    """ This is an empty class
    It has a size attribute as the private attribute
    """

    def __init__(self, size = 0):
        """The initualizer for size

        args:
            size(int): the width of the sqyare
        """

        if (type(size) is not int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
