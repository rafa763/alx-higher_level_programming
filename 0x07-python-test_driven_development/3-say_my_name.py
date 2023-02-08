#!/usr/bin/python3
"""print passed name in a sentence"""


def say_my_name(first_name, last_name=""):
    """
    print the passed first name and last name
    Args:
        param1 (first_name)
        param2 (last_name)
    Exception:
        TypeError: if either first_name or last_name is not a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
