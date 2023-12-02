#!/usr/bin/python3
# delete a key using methods
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    return (a_dictionary)
