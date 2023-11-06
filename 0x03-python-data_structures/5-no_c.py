#!/usr/bin/python3
# remove the letter c from the string
def no_c(my_string):
    remstr = my_string.copy()
    for i in remstr:
        if (i == 'c' or i == 'C'):
            remstr.pop(i)
