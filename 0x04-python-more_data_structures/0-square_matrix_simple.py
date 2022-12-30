#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    m = []
    [m.append(list([x**2 for x in y])) for y in matrix]
    return m
