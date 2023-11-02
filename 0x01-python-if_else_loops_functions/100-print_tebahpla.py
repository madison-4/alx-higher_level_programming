#!/usr/bin/python3
# print the alphabet alteranting
for i in range(0, 26):
    temp = ord('z') - i
    if ((i % 2) == 0):
        print(chr(temp), end="")
    if ((i % 2) == 1):
        print(chr(temp - 32), end="")
