#!/usr/bin/python3
# This task is about printing elements of a list

def safe_print_list(my_list=[], x=0):
    num = 0
    for i in range(0, x):
        try:
            print(i)
            num += 1
        except NameError:
            continue
    return (num)
