#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for li in matrix:
        for j in range(len(li)):
            print("{}".format(li[j]), end="")
            if j < len(li) - 1:
                print(" ", end="")
        print()
