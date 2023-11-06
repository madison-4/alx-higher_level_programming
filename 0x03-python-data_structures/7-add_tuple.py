#!/usr/bin/python3
# add two tuples


def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) < 2):
        r = len(tuple_a)
        if (r == 0):
            tuple_a = (0, 0)
        else:
            tuple_a += (0,)
    if ((len(tuple_b)) < 2):
        if ((len(tuple_b)) == 0):
            tuple_b = (0, 0)
        else:
            tuple_b += (0,)
    sum_list = sum(tuple_a[0], tuple_b[0])
    sum_list2 = sum(tuple_a[1], tuple_b[2])
    return (sum_list, sum_list2)
