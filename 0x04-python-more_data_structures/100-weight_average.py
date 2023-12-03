#!/usr/bin/python3
# advanced task
# give weighted average
def weight_average(my_list=[]):
    ave, su, t = 0, 0, 1
    if (len(my_list) == 0):
        return (0)
    for tup in my_list:
        t = 1
        for tu in tup:
            t *= tu
        su += tup[1]
        ave += t
    mean = ave / su
#    print(su)
    return (mean)
