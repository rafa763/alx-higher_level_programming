#!/usr/bin/python3
"""inspect an object"""


def inherits_from(obj, a_class):
    """
    checks if the passed object is an instance of a class
    that inherited from specified class
    Args:
        param1 (obj): the bassed object
        param2 (a_class): the supposed class of passed object
    Return:
        True: if obj is instance of a_class that inherted form specified class
        False: if obj is not an instance of a_class
    """
    if type(obj) == a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
