#!/usr/bin/python3
"""class Square that defines and checks a square"""


class Square:

    """initialize the class

    Args:
        param1 (size): lenght of the square side
    """
    def __init__(self, size=0):
        self.__size = size

    """size getter"""
    @property
    def size(self):
        return self.__size

    """size setter"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """public method to calc. area"""
    def area(self):
        return (self.__size ** 2)
