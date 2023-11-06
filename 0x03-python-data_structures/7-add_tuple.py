#!/usr/bin/python3
# add two tuples


def add_tuple(tuple_a=(), tuple_b=()):
    sum_list = []
    for i in range(0, 2):
        if (len(tuple_a) < 2):
            r = len(tuple_a) - 1
            for i in range (r, 2):
                tuple_a[i] = 0
        if (len(tuple_b) < 2):
            t = len(tuple_b) - 1
            for j in range(t, 2):
                tuple_b[j] = 0
        sum_list.append(tuple_a[i] + tuple_b[i])
