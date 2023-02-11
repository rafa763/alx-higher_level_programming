#!/usr/bin/python3
"""File IO"""


import json


def load_from_json_file(filename):
    """create an object from JSON file
    Args:
        filename: name of the file to read from
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        data = f.read()
        return json.loads(data)
