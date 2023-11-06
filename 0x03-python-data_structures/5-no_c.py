#!/usr/bin/python3
# remove the letter c from the string
def no_c(my_string):
    if my_string:
        str_list = list(my_string)
        looplist = str_list.copy()
        for letter in looplist:
            if (letter == 'C' or letter == 'c'):
                looplist.remove(letter)
        new_str = ''.join([str(x) for x in looplist])
        return (new_str)
