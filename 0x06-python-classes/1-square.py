#!/usr/bin/python3
"""xDefine a square class that takes a square
The sqaure class is empty
"""


class Square:
    """ This is an empty class
    It has a size attribute as the private attribute
    """

    def __init__(self, size):
        """The initualizer for size

        args:
            size(int): the width of the sqyare
        """
        self.__size = size
