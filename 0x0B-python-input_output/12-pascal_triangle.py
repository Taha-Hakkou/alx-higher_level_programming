#!/usr/bin/python3
"""
12-pascal_triangle.py
"""


def pascal_triangle(n):
    """Returns: list of lists of integers representing
    the Pascal’s triangle of n & an empty list if n <= 0"""
    pascal = []
    pascal.append([1])
    pascal.append([1, 1])
    for i in range(2, n):
        p = pascal[-1]
        pascal.append([1] + [p[i] + p[i - 1] for i in range(1, len(p))] + [1])
    return (pascal)
