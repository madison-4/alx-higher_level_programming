#!/usr/bin/python3
"""A moduel to modify a strig based on special characters
"""


def text_indentation(text):
    """function to print newline after the special chars
    """

    if (type(text) is not str):
        raise TypeError('text must be a string')
    count = 0
    for e in text:
        if (e in ['.', '?', ':']):
            print(e)
            count += 1
            print()
            count += 1
            continue
        elif (e == ' '):
            if (text[count - 1] == '\n'):
                continue
            else:
                print(e, end='')
                count += 1
        else:
            print(e, end='')
            count += 1
            continue
