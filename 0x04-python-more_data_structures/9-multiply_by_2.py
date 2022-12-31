#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    d = {}
    for x, y in a_dictionary.items():
        d[x] = y * 2
    return d
