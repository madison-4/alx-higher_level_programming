#!/usr/bin/python3
# update dictionaries
def update_dictionary(a_dictionary, key, value):
    new_dic = {key : value}
    return (dict(a_dictionary.update(new_dic)))
