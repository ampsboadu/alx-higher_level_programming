#!/usr/bin/python3
"""
Module 2-matrix_divided
Contain a method that return list of division
on matrix: list
Accepts a list and an int as args
"""


def matrix_divided(matrix, div):
    """ return new matrix of matrix / div """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    msg = 'matrix must be a matrix (list of lists) of integers/floats'
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(msg)
        if len(rows) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        
        lst = []
        for val in rows:
            if not isinstance(val, (int, float)):
                raise TypeError(msg)
            lst.append(round(val / div, 2))

        result.append(lst)
    return result
