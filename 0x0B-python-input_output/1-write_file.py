#!/usr/bin/python3
"""file IO"""


def write_file(filename="", text=""):
    """write a string to a text file 
    Args:
        filename: the name of the file to read form
    Return:
        the number of chars written to the file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
