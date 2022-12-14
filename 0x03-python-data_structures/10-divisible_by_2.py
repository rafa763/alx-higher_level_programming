#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    li = []
    for i in my_list:
        if i % 2 == 0:
            li.append(True)
        else:
            li.append(False)
    return (li)
