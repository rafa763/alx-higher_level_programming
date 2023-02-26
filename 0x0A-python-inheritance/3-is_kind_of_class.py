#!/usr/bin/python3
"""check if object is instance of class/inherted class"""


def is_kind_of_class(obj, a_class):
    """
    checks if the passed object is an instance of a class
    or instance of inherted class
    Args:
        param1 (obj): the bassed object
        param2 (a_class): the supposed class of passed object
    Return:
        True: if obj is instance of a_class
        False: if obj is not an instance of a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
