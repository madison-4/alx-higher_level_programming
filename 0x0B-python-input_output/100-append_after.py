#!/usr/bin/python3
""" A module to append text after a given string
"""


def append_after(filename="", search_string="", new_string=""):
    """ Function to append the text
    Args:
    filename: path to file
    search_string: string to append after
    new_string: string to append
    """

    with open(filename, 'a+',encoding="utf-8") as fildes:
        for l in fildes:
            line = fildes.readline()
            if (line == search_string):
                fildes.write(line)
