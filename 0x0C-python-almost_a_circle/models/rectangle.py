#!/usr/bin/python3
"""Inherit from base class"""

from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base class
    Args:
        width: width of the rectangle
        height: height of the rectangle
        x: _
        y: _
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """
    width getter method
    Returns:
        return value of width
    """
    @property
    def width(self):
        return self.__width

    """
    width setter method
    Args:
        width: value to assign for rectangle width
    Exceptions:
        TypeError: if width is not an integer
        ValueError: if width is less than or equal to zero
    """
    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    """
    height getter method
    Return:
        value of height
    """
    @property
    def height(self):
        return self.__height

    """
    height setter method
    Args:
        height: value to assign for rectangle height
    Exceptions:
        TypeError: if height is not an integer
        ValueError: if height is less than or equal to zero
    """
    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    """
    x getter method
    Return:
        value of x
    """
    @property
    def x(self):
        return self.__x

    """
    x setter method
    Args:
        x: value to assign for x
    Exceptions:
        TypeError: if x is not an integer
        ValueError: if x is less than zero
     """
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """
    y getter method
    Return:
        value of y
    """
    @property
    def y(self):
        return self.__y

    """
    y setter method
    Args:
        x: value to assign for x
    Exceptions:
        TypeError: if x is not an integer
        ValueError: if x is less than zero
    """
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """
    calclate area method
    Returns:
        area of the rectangle
    """
    def area(self):
        return self.__width * self.__height
