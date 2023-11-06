#!/usr/bin/python3
# print ints in a list in reverse
def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    new_list = my_list.reverse()
    for i in range(0, size):
        print("{:d}".format(new_list[i])
