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
                  x: private isntance attribute showing x point
                  y: point on rectangle
                  id of the rectangle object
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for the wisth class
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """ A setter for the width value
        """

        self.__width = value
        return (self.__width)

    @property
    def height
    
