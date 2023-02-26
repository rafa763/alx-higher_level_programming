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

    def to_json(self):
        return self.__dict__
