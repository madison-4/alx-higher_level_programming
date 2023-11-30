#!/usr/bin/python3
# Find and replace all occurrences of an element
def search_replace(my_list, search, replace):
    newlist = []
    for i in my_list:
        if i == search:
            newlist.append(replace)
            continue
        newlist.append(i)
    return newlist
