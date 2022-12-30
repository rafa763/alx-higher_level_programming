#!/usr/bin/python3

def search_replace(my_list, search, replace):
    m = []
    for x in my_list:
        if x == search:
            m.append(replace)
        else:
            m.append(x) 
    return m
