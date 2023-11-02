#!/usr/bin/python3
def islower(c):
    value = ord(c)
    if ((value >= 97) and (value < 123)):
        return (True)
    else:
        return (False)
def uppercase(str):
    temp = list(str)
    for i in temp:
        if ((islower(i))):
            temp[i] = i + 32
        temp[i] = i
    return (temp)
