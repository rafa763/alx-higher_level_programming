#!/usr/bin/python3

def uniq_add(my_list=[]):
    l = list(set(my_list))
    n = 0
    for x in l:
        n += x
    return n
