#!/usr/bin/python3
# multiply only values by 2
def multiply_by_2(a_dictionary):
    rect = [ke for ke in a_dictionary.keys()]
    val = [va for va in a_dictionary.values()]
    vals = [x * 2 for x in val]
    res = {rect[i]:vals[i] for i in range(len(rect))}
    return (res)
