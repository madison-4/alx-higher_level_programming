#!/usr/bin/python3

# an attempt at making a singly lunked list
class Node:
    """ This is a class for a node of a singly linked list
    """
    
    def __init__(self, data, next_node=None):
        """This function is to initualize the node class
        """

        if (type(data) is not int):
            raise TypeError('data must be an integer')
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """This is a getter for the data variable
        """
        return (self.__data)

    @property
    def next_node(self):
        """A getter for the next node class
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """A setter for the next node
        """
        if ((type(value) is not None) and (type(value) is not Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    head = None

    def __init__(self):
