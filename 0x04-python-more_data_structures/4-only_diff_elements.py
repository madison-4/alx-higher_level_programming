#!/usr/bin/python3
# get common elements in only one list
# I dislike this brute force method
def only_diff_elements(set_1, set_2):
    ret = []
    for elem in set_1:
        if elem not in set_2:
            ret.append(elem)
    for el in set_2:
        if el not in set_1:
            ret.append(el)
    return (set(ret))
