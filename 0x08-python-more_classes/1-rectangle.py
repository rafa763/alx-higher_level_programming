#!/usr/bin/python3
"""define class rectangle"""


class Rectangle:

    """initialize the class

    Args:
        param1 (width): width of the rectangle
        param2 (height): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    """width getter"""
    @property
    def width(self):
        return (self.__width)

    """width setter"""
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """height getter"""
    @property
    def height(self):
        return self.__height

    """height getter"""
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
