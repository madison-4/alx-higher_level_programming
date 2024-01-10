#!/usr/bin/python3
"""A module to define a rectangle class based on 0-rectangle.py
"""


class Rectangle:
    """A class for the rectangle objects
    """

    def __init__(self, width=0, height=0):
        """initializer function for the class
        """

        if (type(width) is not int):
            raise TypeError('width must be an integer')
        if (width < 0):
            raise ValueError('width must be >= 0')
        if (type(height) is not int):
            raise TypeError('height must be an integer')
        if (height < 0):
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter for the width attribute
        """

        if ((type(value)) is not int):
            raise TypeError('width must be an integer')
        if (value < 0):
            raise ValueError('width must be >= 0')
        self.__width = value
        return (self.__width)

    @property
    def height(self):
        """height getter for the rectangle
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """set the height of the rectangle
        """

        if ((type(value)) is not int):
            raise TypeError('height must be an integer')
        if (value < 0):
            raise ValueError('height must be >= 0')
        self.__height = value
        return (self.__height)

    def area(self):
        """get the rectangle area
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """get the rectangle perimeter
        """

        if ((self.__height == 0) or (self.__width == 0)):
            return (0)
        else:
            return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """ Prints the rectangle based on width and height
        """

  tre = ''      

tr = [['#' for t in range(self.__width)]for tree in range (self.__height)]
        tr = tr.join(' ')

        return (str(tr))
