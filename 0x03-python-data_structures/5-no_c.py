#!/usr/bin/python3
# remove the letter c from the string
def no_c(my_string):
    if my_string:
        str_list = list(my_string)
        new_str = ''
        looplist = str_list.copy()
        for letter in looplist:
            if (letter == 'C' or letter == 'c'):
                looplist.remove(letter)
        for let in looplist:
            new_str += let
        return (new_str)
    else:
        return (my_string)
