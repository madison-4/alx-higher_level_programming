#!/usr/bin/python3
# remove the letter c from the string
def no_c(my_string):
    if my_string:
        str_list = list(my_string)
        print(str_list)
        looplist = str_list.copy()
        for letter in looplist:
            looplist.remove('c')
            looplist.remove('C')
        print(looplist)
no_c("C c is cfun not c too")
