#!/usr/bin/python3
# print a dict soprted by keys
def print_sorted_dictionary(a_dictionary):
    ret = dict(sorted(a_dictionary.items()))
#    print(ret)
    for i, k in ret.items():
        print(f"{i}: {k}")
