#!/usr/bin/python3
"""base class"""


class BaseGeometry:
    """method that raises exception"""
    def area(self):
        raise Exception("area() is not implemented")
