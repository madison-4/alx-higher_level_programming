#!/usr/bin/python3
# convert to arabic numbers from roman numbers
def roman_to_int(roman_string):
    romint = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,'D': 500, 'M': 1000}
    s, value = 0, 0
    place1 = 0
    if not roman_string:
        return 0
    while (s < (len(roman_string))):
        value1 = romint.get(roman_string[s])
        if ((s + 1) < len(roman_string)):
            value2 = romint.get(roman_string[s + 1])
            if (value1 >= value2):
                value += value1
                s += 1
                continue
            else:
                value += (value2 - value1)
                s += 2
                continue
        else:
            value += value1
            s += 1
            continue
    return (value)
