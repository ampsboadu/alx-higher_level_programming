#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        lght = len(row) - 1
        i = 0
        while i <= lght:
            if i == lght:
                print("{:d}".format(row[i]), end="")
            else:
                print("{:d}".format(row[i]), end=" ")
            i += 1
        print()
