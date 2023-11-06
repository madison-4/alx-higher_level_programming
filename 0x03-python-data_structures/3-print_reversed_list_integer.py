#!/usr/bin/python3
# print ints in a list in reverse
def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
