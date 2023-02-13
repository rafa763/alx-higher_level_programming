#!/usr/bin/python3
"""base class"""


class Base:
    __nb_objects = 0
    """
    Assign id value based on the passed argument
    Args:
        id: the id of the created instance
        nb_objects: no of the created instances
    """
    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
