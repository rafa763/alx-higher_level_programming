#!/usr/bin/python3
"""file IO"""


def read_file(filename=""):
    """ read a text file and print it to stdout
    Args:
        filename: the name of the file to read form
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
