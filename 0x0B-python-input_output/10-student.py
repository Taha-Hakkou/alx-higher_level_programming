#!/usr/bin/python3
"""
10-student.py
"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """instantiates new student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of student object"""
        dlist = list(self.__dict__.items())
        if type(attrs) == list and all([type(s) == str for s in attrs]):
            return (dict(filter((lambda s: s[0] in attrs), dlist)))
        return (self.__dict__)
