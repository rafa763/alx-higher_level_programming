#!/usr/bin/python3
"""define class rectangle"""


class Rectangle:

    """initialize the class

    Args:
        param1 (width): width of the rectangle
        param2 (height): height of the rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    def __repr__(self):
        return ("{}({}, {})".format(self.__class__.__name__,
                self.__width, self.__height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    """area method"""
    def area(self):
        return (self.__height * self.__width)

    """perimeter method"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    """print rectangle"""
    def __str__(self):
        s = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            for i in range(self.__height):
                for i in range(self.__width):
                    s += str(self.print_symbol)
                s += "\n"
            return (s[:-1])

    """compare two rectangles"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return (rect_1)
        elif rect_1.area() < rect_2.area():
            return (rect_2)
        else:
            return (rect_1)

    """convert rectangle"""
    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
