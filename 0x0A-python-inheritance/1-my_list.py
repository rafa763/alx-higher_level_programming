#!/usr/bin/python3
"""class that inherits form list"""


class MyList(list):
    """method to sort the list"""
    def print_sorted(self):
        print(sorted(self))

    def __str__(self):
        return "{} converts unsorted list into sorted list".format(type(self).__name__)
