#!/usr/bin/python3
# Prints a value ensuring it's an integer
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        return (False)
