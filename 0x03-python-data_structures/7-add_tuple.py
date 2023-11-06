#!/usr/bin/python3
# add two tuples


def add_tuple(tuple_a=(), tuple_b=()):
    sum_list = []
    for i in range(0, 2):
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
        sum_list.append(tuple_a[i] + tuple_b[i])
        sum_list = tuple(sum_list)
    return (sum_list)
