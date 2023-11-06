#!/usr/bin/python3
# remove the letter c from the string
def no_c(my_string):
    if my_string:
        str_list = list(my_string)
        new_str = ''
        print(str_list)
        looplist = str_list.copy()
        for letter in looplist:
            if (letter == 'C' or letter == 'c'):
                looplist.remove(letter)
        for char in looplist:
            new_str += char
        return (new_str)
