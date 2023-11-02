#!/usr/bin/python3
# remove a character from a particular array
# of course, since strings are immutable
# a new string will be returned
def remove_char_at(str, n):
    if (n >= 0):
        newstr = str[:n] + str[(n + 1):]
        return (newstr)
    return (str)
