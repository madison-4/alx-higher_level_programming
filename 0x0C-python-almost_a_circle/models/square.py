#!/usr/bin/python3
import rectangle
""" A sqaure class that inherits from rectangle
"""

class Square(rectangle.Rectangle):
    """ A special rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization inheriting from super
        """

        super().__init__(size, id, x, y)
        size = super().__init__(width, height)

    def __str__(self):
        """ override different string methiods
        """
        
