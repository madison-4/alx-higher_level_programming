#!/usr/bin/python3
"""This module is for  is for making linked lists in python
"""


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

    @data.setter
    def data(self, value):
        """set the data value to value
        """

        if (type(value) is not int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """A getter for the next node class
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """A setter for the next node
        """

        if ((type(value) not in [None, Node])):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """the linked list class
    """

    def __init__(self):
        """struccture for the singly-linked list
        """

        self.head = None

    def sorted_insert(self, value):
        """function to insert and sort values
        """

        new = Node(value, None)
        if (self.head is None):
            self.head = new
            return
        else:
            temp = self.head
            prev = temp
            while (temp is not None):
                if (temp.data < new.data):
                    prev = temp
                    temp = temp.next_node
                else:
                    break
            if (temp is None):
                prev.next_node = new
                return
            if (temp == self.head):
                new.next_node = temp
                self.head = new
                return
            new.next_node = temp
            prev.next_node = new

    def __str__(self):
        """dunder method to print list
        """

        temp = self.head
        out = ""

        while (temp is not None):
            out += str(temp.data) + "\n"
            temp = temp.next_node
        return (out[:-1])
