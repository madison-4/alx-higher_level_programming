#!/usr/bin/python3
# A fuction to print a lists of list as a matrix
# Am to impement a matrix printed as on paper


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (j != (len(matrix[i]) - 1)):
                endchar = ' '
            else:
                endchar = ''
            print("{:d}".format(matrix[i][j]), end=end_char)
        print("")
