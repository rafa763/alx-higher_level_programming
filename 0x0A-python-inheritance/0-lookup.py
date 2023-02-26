#!/usr/bin/python3
"""Return a list of available attributes and methods of the object"""


def lookup(obj):
    """Return a list of available attributes and methods of the object"""
    return (dir(obj))
