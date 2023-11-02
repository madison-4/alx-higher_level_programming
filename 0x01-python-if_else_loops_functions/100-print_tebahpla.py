#!/usr/bin/python3
# print the alphabet alteranting
for i in range(0, 26):
    temp = ord('z') - i
    if ((i % 2) == 0):
        print("{}".format(chr(temp)), end="")
    if ((i % 2) == 1):
        print("{}".format(chr(temp - 32)), end="")
