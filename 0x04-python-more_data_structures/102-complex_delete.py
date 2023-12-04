#!/usr/bin/python3
# practice getting a key with a given value
def complex_delete(a_dictionary, value):
    for t, i in a_dictionary.items():
        keys = []
        if (value == i):
            keys.append(t)
    for u in keys:
        a_dictionary.pop(u)
    return (a_dictionary)
