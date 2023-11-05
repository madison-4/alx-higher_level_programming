#!/usr/bin/python3
# retrieve an element from a list
def element_at(my_list, idx, element):
    if (idx < 0):
        return (None)
    length = len(my_list)
    if (idx >= length):
        return (None)
    my_list[idx] = element
