#!/usr/bin/python3
"""inherited class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    create inherited class from BaseGeometry
    which is the base class in this case
    Args:
        param1 (width): width of the rectangle
        param2 (height): height of the rectangle
    Exceptions:
        TypeError: if value is not an integer
        ValueError: if value is less than or equal to zero
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    """return area of rectangle"""
    def area(self):
        return (self.__width * self.__height)

    """print dimensions"""
    def print(self):
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
