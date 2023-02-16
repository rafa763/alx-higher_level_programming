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

    def update(self, *args, **kwargs):
        """
        update the square parameters dynamically
        """
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                    self.height = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        return the dictionary representation of a Square
        """
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
