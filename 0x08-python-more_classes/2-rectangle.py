#!/usr/bin/python3
"""
2-rectangle.py
"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """instantiates rectangle object with optional width & height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """width property setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """height property setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.height * self.width)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.height == 0 or self.width == 0:
            return (0)
        return (2 * (self.height + self.width))
