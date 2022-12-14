#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    b = [] 
    x = (list(tuple_a) + [0] * 2)[0:2] 
    y = (list(tuple_b) + [0] * 2)[0:2]
    for i in {0, 1}:
        b.append(x[i] + y[i])
    return tuple(b) 
