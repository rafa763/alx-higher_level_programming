#!/usr/bin/python3
"""base class"""


class BaseGeometry(object):
    """
    initialize the class
    """
    def __init(self, name, value):
        self.name = name
        self.value = value

    """
    validate the passed integer
    Args:
        param1 (name): the name of the passed integer
        param2 (value): the value of the name
    Exceptions:
        TypeError: if value is not an integer
        ValueError: if value is less than or equal to zero
    """
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    """method that raises exception"""
    def area(self):
        raise Exception("area() is not implemented")
