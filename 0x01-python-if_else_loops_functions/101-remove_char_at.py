#!/usr/bin/python3
# remove a character from a particular array
# of course, since strings are immutable
# a new string will be returned
def remove_char_at(str, n):
    for i in str:
        if (i != (n + 1)):
            newstr = newstr + str[i]
    return (newstr)
