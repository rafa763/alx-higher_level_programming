#!/usr/bin/python3
"""inherited class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    create inherited class from rectangle
    which is the base class in this case
    Args:
        param1 (size): length of the side
    Exceptions:
        TypeError: if value is not an integer
        ValueError: if value is less than or equal to zero
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    """return area of rectangle"""
    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
