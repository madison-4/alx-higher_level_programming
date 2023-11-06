#!/usr/bin/python3
# remove the letter c from the string
def no_c(my_string):
    if my_string:
        cap_list = ''
        new_str = ''
        str_list = my_string.split('c')
        print(str_list)
        for i in str_list:
            if (i == 'c'):
                new_str += ''
            else:
                new_str += i
        for car in new_str:
            if (car == 'C'):
                cap_list += ''
            else:
                cap_list += car
        print(cap_list)
no_c("C c is cfun not c too")
