#!/usr/bin/python3
# print to stdout without eval, print or sys module
import os
os.write(1, b'#pythoniscool\n')
