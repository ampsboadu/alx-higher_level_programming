#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_matirx = []
    for row in matrix:
        in_matrix = []
        for i in row:
            in_matrix.append(i * i)
        sqr_matirx.append(in_matrix)
    return sqr_matirx
