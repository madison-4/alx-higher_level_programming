#!/usr/bin/python3
# A fuction to print a lists of list as a matrix
# Am to impement a matrix printed as on paper


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        sub_len = len(matrix[i])
        for j in range(sub_len):
            if j != sub_len - 1:
                end_char = ' '
            else:
                end_char = ''
            print("{:d}".format(matrix[i][j]), end=end_char)
        print("")
