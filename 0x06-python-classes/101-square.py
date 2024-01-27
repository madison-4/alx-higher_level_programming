#!/usr/bin/python3
"""xDefine a square class that takes a square
The sqaure class is empty
"""


class Square:
    """ This is an empty class
    It has a size attribute as the private attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """The initualizer for size

        args:
            size(int): the width of the sqyare
        """

        if (type(size) is not int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
        if (type(position) is not tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if ((type(position[0]) is not int) or (type(position[1]) is not int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        if ((position[0] < 0) or (position[1] < 0)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

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

    def my_print(self):
        """ print a square with # for this square
        """
        if (self.__size == 0):
            print()
            return (0)
        for t in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for y in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print('#', end='')
            print()

    @property
    def position(self):
        """ getter for the position tuple
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ setter for the position attribute
        """
        if (type(value)) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if (len(value) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        if ((type(position[0]) is not int) or (type(position[1]) is not int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        if (position[0] < 0 or position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
        return (self.__position)

    def __str__(self):
        """describe how to print instances of this class
        """
        out = ""
        if (self.__size == 0):
            out = "\n"
            return (out)
        for t in range(self.__position[1]):
            out += "\n"
        for r in range(self.__size):
            for e in range(self.__position[0]):
                out += " "
            for d in range(self.__size):
                out += "#"
            out += "\n"
        return (out[:-1])
