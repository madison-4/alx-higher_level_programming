#!/usr/bin/python3
"""A module to define a rectangle class based on 0-rectangle.py
"""


class Rectangle:
    """A class for the rectangle objects
    """

    number_of_instances = 0
    print_symbol = '#'

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
        type(self).number_of_instances += 1

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

        if (self.__height == 0 or self.__width == 0):
            return ""
        tre = []
        for t in range(self.__height):
            for tree in range(self.__width):
                tre.append(str(type(self).print_symbol))
            if (t != (self.__height - 1)):
                tre.append('\n')
        return ("".join(tre))

    def __repr__(self):
        """give str rep back
        """

        tre = ''
        tre += 'Rectangle(' + str(self.__width)
        tre += ', ' + str(self.__height) + ')'
        return (tre)

    def __del__(self):
        """What to do on deletetion
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
