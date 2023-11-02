#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
remainder = number % 10
if (number < 0):
    number = -number
    remainder = number % 10
    remainder = -remainder
    number = -number
print(f'Last digit of {number:d} is', end=' ')
if ((number % 10) > 5):
    print(f'{remainder:d} and is greater than 5')
elif ((number % 10) == 0):
    print(f'{remainder:d} and is 0')
elif (remainder < 6) and (remainder != 0):
    print(f'{remainder: d} and is less than 6 and not 0')
