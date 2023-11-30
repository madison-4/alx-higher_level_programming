#!/usr/bin/python3
# get common elements in only one list
# I dislike this brute force method
def only_diff_elements(set_1, set_2):
    ret = []
    for elem in set_1:
        for el in set_2:
            if (elem == el):
                break
            ret.append(elem)
            ret.append(el)
    return (set(ret))
