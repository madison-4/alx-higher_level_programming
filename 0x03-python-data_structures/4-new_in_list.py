#!/usr/bin/python3
# retrieve an element from a list
def new_in_list(my_list, idx, element):
    if (idx < 0):
        return (my_list.copy())
    length = len(my_list)
    if (idx >= length):
        return (my_list.copy())
    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
