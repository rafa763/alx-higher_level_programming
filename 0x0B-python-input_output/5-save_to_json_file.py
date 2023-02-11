#!/usr/bin/python3
"""file IO"""


import json

def save_to_json_file(my_obj, filename):
    """
    write an Object to a text file, using a JSON representation
    Args:
        my_obj: the object to be written to the file
        filename: name of the file to write to
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        data = json.dumps(my_obj)
        f.write(data)
