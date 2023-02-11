#!/usr/bin/python3
"""file IO"""


def append_write(filename="", text=""):
    """append a string to a text file
    Args:
        filename: the name of the file to append to
    Return:
        the number of chars written to the file
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
