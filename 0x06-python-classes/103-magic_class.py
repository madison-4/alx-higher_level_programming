#!/usr/bin/python3
""" A recreation of a python class seeing its bytecodes
"""


from math import pi
""" import the math module to use its pi constant
"""


class MagicClass:
    """a class for a python bytecode
    """

    def __init__(self, radius=0):
        """ initializer fr the class
        """

        if (type(radius) not in [int, float]):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ A fuction to get te area of the circlr
        """

        return ((self.__radius ** 2) * pi)

    def circumference(self):
        """ A function to get tye circumference of the circle
        """

        return ((2 * pi) * self.__radius)
