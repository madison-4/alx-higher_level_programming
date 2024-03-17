#!/usr/bin/python3
import base
""" A module to create the rectangle class
"""


class Rectangle(base.Base):
    """ A class that inherots from the base and makes a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The constructor for the Rectangle class
            Args:
                  width: private isntance attribute, width of rectangle
                  height: height of the rectangle
