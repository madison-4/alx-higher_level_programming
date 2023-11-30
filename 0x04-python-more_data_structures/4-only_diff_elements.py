#!/usr/bin/python3
# get common elements in only one list
# I dislike this brute force method
def only_diff_elements(set_1, set_2):
    ret = []
    for elem in set_1:
        valret = 0
        for el in set_2:
            if (elem == el):
                valret = 1
                break
            ret.append(el)
        if (valret == 0):
            ret.append(elem)
    return (set(ret))
