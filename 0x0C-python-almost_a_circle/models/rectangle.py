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
    def height(self):
        """ A getter for the height property of te class
        """

        return (self.__height)
    
    @height.setter
    def height(self, value):
        """ A setter for the height property
        """

        self.__height = value
        return (self.width)
    
    @property
    def x(self):
        """ Getter for the x value"""

        return (self.__x)
    
    @x.setter
    def x(self, value):
        """ Setter for the x value
        """

        self.__x = value
        return (self.__x)
    
    @property
    def y(self):
        """ A getter for the y attribute
        """

        return (self.__y)

    @y.setter
    def y(self, value):
        """ A setter for the y attribute
        """ 

        self.__y = value
        return (self.__y)
    