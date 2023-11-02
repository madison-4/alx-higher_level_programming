#!/usr/bin/python3
# print the last digit of a number

def print_last_digit(number):
    remainder = ((abs(number)) % 10)
    print(f'{(abs(number)) % 10}', end="")
    if (number < 0):
        return (remainder)
    return (remainder)
