#!/usr/bin/python3
"""create base class"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__+'.json', mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = []
                for i in list_objs:
                    dict_list.append(i.to_dictionary())
                f.write(Base.to_json_string(dict_list))
