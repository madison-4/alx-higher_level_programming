#!/usr/bin/python3
# get the highest score
def best_score(a_dictionary):
    large = 0
    if not a_dictionary:
        return (None)
    num_list = [num for val, num in a_dictionary.items()]
    for num in num_list:
        if (num > large):
            large = num
    numlarge = [i for i, ke in a_dictionary.items() if ke == large]
    res = numlarge[0]
    return (res)
