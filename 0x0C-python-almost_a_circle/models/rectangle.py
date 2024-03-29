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
        for i in range(self.y):
            print()
        for i in range(self.height):
            for i in range(self.x):
                print(' ', end='')
            for i in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        update the arguments of the current rectangle
        if args are passed kwargs are skipped
        """
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    if args is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
                i += 1
        else:
            if kwargs is None:
                self.__init__(self.width, self.height, self.x, self.y)
            else:
                for i in kwargs.items():
                    if i[0] == 'x':
                        self.__x = i[1]
                    elif i[0] == 'y':
                        self.__y = i[1]
                    elif i[0] == 'width':
                        self.__width = i[1]
                    elif i[0] == 'height':
                        self.__height = i[1]
                    elif i[0] == 'id':
                        self.id = i[1]

    def to_dictionary(self):
        """
        return the dictionary representation of a Rectangle
        """
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
