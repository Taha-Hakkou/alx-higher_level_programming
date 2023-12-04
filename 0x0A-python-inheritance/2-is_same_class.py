#!/usr/bin/python3
"""
2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """returns True if object is exactly an instance of a_class;
    otherwise False"""
    if type(obj) == a_class:
        return (True)
    return (False)
