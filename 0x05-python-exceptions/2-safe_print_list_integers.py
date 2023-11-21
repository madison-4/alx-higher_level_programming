#!/usr/bin/python3
# This task is about printing elements of a list

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            num += 1
        except (NameError, IndexError, TypeError, ValueError, RuntimeError):
            continue
    print()
    return (num)
