#!/usr/bin/python3
"""print a square"""


def print_square(size):
    """
    print a square with the character #
    Args:
        param1 (size): length of the square side
    Exceptions:
        TypeError: if size is not an integer or a float less than zero
        ValueError: if the size is less than zero
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
