#!/usr/bin/python3
"""Inherit from base class"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """width getter method"""
    @property
    def width(self):
        return self.__width

    """width setter method"""
    @width.setter
    def width(self, width):
        self.__width = width

    """height getter method"""
    @property
    def height(self):
        return self.__height

    """height setter method"""
    @height.setter
    def height(self, height):
        self.__height = height

    """x getter method"""
    @property
    def x(self):
        return self.__x

    """x setter method"""
    @x.setter
    def x(self, value):
        self.__x = value

    """y getter method"""
    @property
    def y(self):
        return self.__y

    """y setter method"""
    @y.setter
    def y(self, value):
        self.__y = value
