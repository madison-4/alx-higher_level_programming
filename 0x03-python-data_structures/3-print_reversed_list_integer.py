#!/usr/bin/python3
# print ints in a list in reverse
def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    my_list.sort()
    for i in range(0, size):
        print("{:d}".format(my_list[i])
