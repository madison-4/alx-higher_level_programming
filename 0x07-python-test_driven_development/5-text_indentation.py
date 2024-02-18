#!/usr/bin/python3
"""A moduel to modify a strig based on special characters
"""


def text_indentation(text):
    """function to print newline after the special chars
    """

    if (type(text) is not str):
        raise TypeError('text must be a string')
    for e in text:
        if (e in ['.', '?', ':']):
            print(e)
            print()
            continue
        elif (e == ' '):
            continue
        else:
            print(e, end='')
