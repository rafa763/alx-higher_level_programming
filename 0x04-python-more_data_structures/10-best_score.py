#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    return (list(sorted(a_dictionary.items()))[-1][0])
