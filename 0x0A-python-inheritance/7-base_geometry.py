#!/usr/bin/python3
"""
7-base_geometry.py
"""


class BaseGeometry:
    """base geometry class"""

    def area(self):
        """raises Exception with message 'area() is not implemented'"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates 'value'"""
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
