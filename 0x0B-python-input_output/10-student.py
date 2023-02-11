#!/usr/bin/python3
"""Student class"""


class Student:
    """
    initialize the student class
    Args:
        first_name: the student first name
        last_name: the student last name
        age: the student age
    Return:
        dictionary representation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs and type(attrs) == list:
            attr_list = {}
            for key in attrs:
                if hasattr(self, key):
                    attr_list[key] = getattr(self, key)
            return attr_list
        return self.__dict__
