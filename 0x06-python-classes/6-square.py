#!/usr/bin/python3
"""class Square that defines and checks a square"""


class Square:

    """initialize the class

    Args:
        param1 (size): lenght of the square side
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """size getter"""
    @property
    def size(self):
        return self.__size

    """size setter"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """position getter"""
    @property
    def position(self):
        return self.__position

    """position setter"""
    @position.setter
    def position(self, value):
        if (value[0] < 0) or (value[1] < 0) or (type(value[0]) != int) or (type(value[1]) != int) or (type(value) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
 
    """public method to calc. area"""
    def area(self):
        return (self.__size ** 2)

    """print a square"""
    def my_print(self):
        if self.__size > 0:
            for o in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end='')
                for k in range(self.__size):
                    print("#", end='')
                print('')
        else:
            print('')
