#!/usr/bin/python3
# get common elements in a list
# I dislike this brute force method
def common_elements(set_1, set_2):
    ret = []
    for elem in set_1:
        for el in set_2:
            if (elem == el):
                ret.append(el)
                break
    return (set(ret))
