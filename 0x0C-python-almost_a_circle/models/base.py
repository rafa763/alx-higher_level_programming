#!/usr/bin/python3
"""create base class"""


class Base:
    """
    Assign id value based on the passed argument
    Args:
        id: the id of the created instance
        nb_objects: no of the created instances
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
