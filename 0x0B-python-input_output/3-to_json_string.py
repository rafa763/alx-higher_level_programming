#!/usr/bin/python3
"""JSON representation"""


import json


def to_json_string(my_obj):
    """return JSON representation of passed string
    Args:
        my_object: object passed (string)
    Retrun:
        JSON object
    """
    return json.dumps(my_obj)
