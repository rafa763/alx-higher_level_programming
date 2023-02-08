#!/usr/bin/python3
"""divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Return a new matrix after division
    Args:
        param1 (matrix): the matrix to perform operations on
        param2 (div): the value to divide param1 with
    Exceptions:
        TypeError: if div is neither float nor int, matrix is not a list or
        each row of the matrix doesn't have the same size
        ZeroDivisionError: if div is zero
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")
    ans = []
    length = []
    for li in matrix:
        sub = []
        length.append(len(li))
        for i in li:
            if (type(i) == int or type(i) == float):
                sub.append(round(i / div, 2))
            else:
                raise TypeError("matrix must be a matrix
                                (list of lists) of integers/floats")
        ans.append(sub)

    if len(set(length)) == 1:
        return ans
    else:
        raise TypeError("Each row of the matrix must have the same size")
