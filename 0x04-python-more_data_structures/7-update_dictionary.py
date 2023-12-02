#!/usr/bin/python3
# update dictionaries
def update_dictionary(a_dictionary, key, value):
    new_dict = {key: value}
    a_dictionary.update((new_dict))
    return (a_dictionary)
