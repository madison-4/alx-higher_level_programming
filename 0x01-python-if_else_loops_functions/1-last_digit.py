#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f'Last digit of {number: d} is {int(number % 10): d}', end=' ')
if ((number % 10) > 5):
    print(f'and is greater than 5')
elif ((number % 10) == 0):
    print(f'and is 0')
elif (((number % 10) < 6) && ((number % 10) != 0)):
    print(f'and is less than 6 and not 0')
