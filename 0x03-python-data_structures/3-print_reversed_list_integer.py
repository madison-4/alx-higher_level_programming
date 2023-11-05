#!/usr/bin/python3
# print ints in a list in reverse
def print_reversed_list_integer(my_list=[]):
    length = len(my_list) - 1
    for i in range(length, -1):
        print("{:d}".format(mylist[i]))
