#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    squares = [list(map((lambda i: i ** 2), array)) for array in matrix]
    return (squares)
