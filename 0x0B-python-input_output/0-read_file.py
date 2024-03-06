#!/usr/bin/python3
""" This modulereads a text file and prints it to stdout
"""


def read_file(filename=""):
    """ function to read the file and print it to stdout
    """

    with open(filename, mode='r', encoding='utf-8') as filse:
        return (print(filse.read()))
