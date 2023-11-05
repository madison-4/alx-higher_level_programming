#!/usr/bin/python3
# retrieve an element from a list
def element_at(my_list, idx, element):
    if (idx < 0):
        return (my_list)
    length = len(my_list)
    if (idx >= length):
        return (my_list)
    my_list[idx] = element
