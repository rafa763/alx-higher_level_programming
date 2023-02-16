#!/usr/bin/python3
from models.rectangle import Rectangle
"""Inherit from inherited class"""


class Square(Rectangle):
    """
    Inherit from class Rectangle since Square is just a
    special case of Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize the square by using the parent
        class Rectangle
        """
        super().__init__(size, size, x, y, id)

    def width(self, value):
        """
        initialize the square width using the parent
        class Rectangle
        """
        super().width(value)

    def height(self, value):
        """
        initialize the square height using the parent
        class Rectangle
        """
        super().height(value)

    def x(self, value):
        """
        initialize the square shift x using the parent
        class Rectangle
        """
        super().x(value)

    def y(self, value):
        """
        initialize the square shift y using the parent
        class Rectangle
        """
        super().y(value)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def display(self):
        """
        print Square instance with the character #
        """
        super().display()
