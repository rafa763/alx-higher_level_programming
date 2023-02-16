#!/usr/bin/python3
"""Inherit from inherited class"""


from models.rectangle import Rectangle


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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        """
        set the width and height of the square
        """
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def display(self):
        """
        print Square instance with the character #
        """
        super().display()
