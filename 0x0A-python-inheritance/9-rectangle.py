#!/usr/bin/python3
"""
9-rectangle.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """instantiates rectangle obj with width & height"""
        try:
            self.integer_validator("width", width)
            self.__width = width
            self.integer_validator("height", height)
            self.__height = height
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

    def area(self):
        """returns area of reactangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns rectangle description & make it printable"""
        return (f'[Rectangle] {self.__width}/{self.__height}')
