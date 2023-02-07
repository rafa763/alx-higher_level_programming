#!/usr/bin/python3
"""add 2 integers"""


def add_integer(a, b=98):
    """
    Return the sum of a and b
    floats are casted to ints
    Args:
        param1 (a): first number to be added
        param2 (b): second number to be added
    Eceptions:
        TypeError: if the type of a or b is neither int nor float
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
