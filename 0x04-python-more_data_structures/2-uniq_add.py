#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    n = 0
    for x in new_list:
        n += x
    return n
