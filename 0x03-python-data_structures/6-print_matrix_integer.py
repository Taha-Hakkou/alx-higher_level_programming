#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""
    for list in matrix:
        for integer in list:
            print("{:d}".format(integer), end=" ")
        print()
