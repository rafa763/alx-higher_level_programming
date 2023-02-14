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

    @property
    def width(self):
        """
        width getter method
        Returns:
            return value of width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        width setter method
        Args:
            width: value to assign for rectangle width
        Exceptions:
            TypeError: if width is not an integer
            ValueError: if width is less than or equal to zero
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        height getter method
        Return:
            value of height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        height setter method
        Args:
            height: value to assign for rectangle height
        Exceptions:
            TypeError: if height is not an integer
            ValueError: if height is less than or equal to zero
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        x getter method
        Return:
            value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter method
        Args:
            x: value to assign for x
        Exceptions:
            TypeError: if x is not an integer
            ValueError: if x is less than zero
         """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y getter method
        Return:
            value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter method
        Args:
            x: value to assign for x
        Exceptions:
            TypeError: if x is not an integer
            ValueError: if x is less than zero
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calclate area public method
        Returns:
            area of the rectangle (width * height)
        """
        return self.width * self.height

    def display(self):
        """
        print Rectangle instance with the character #
        """
        for i in range(self.height):
            for i in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
