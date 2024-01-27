#!/usr/bin/python3
"""xDefine a square class that takes a square
The sqaure class is empty
"""


class Square:
    """ This is an empty class
    It has a size attribute as the private attribute
    """

    def __init__(self, size=0):
        """The initualizer for size

        args:
            size(int): the width of the sqyare
        """

        if (type(size) is not int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.size = size

    def area(self):
        """This function gets the area of the sqaure object
        args:
             self(obj): the object of the class
        """

        return (self.__size * self.__size)

    @property
    def size(self):
        """ a getter for the size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ setter for the value of size
        """
        if (type(value) is not int):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value
        return (self.__size)

    def __repr__(self):
        """ get the area to be evaluated when used with an objects
        """

        return (self.__area())
