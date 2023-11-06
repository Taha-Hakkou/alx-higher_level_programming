#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""
    for array in matrix:
        for integer in array:
            print("{:d}".format(integer), end=" ")
        print()
