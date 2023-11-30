#!/usr/bin/python3


"""
This function adds all unique integers in a list
Am going to use the set function
"""


def uniq_add(my_list=[]):
    r = set(my_list)
    su = 0
    for num in r:
        su += num
    return (su)
