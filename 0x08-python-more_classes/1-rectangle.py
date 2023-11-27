#!/usr/bin/python3
"""
1-rectangle.py
"""


class Rectangle:
    """defines a rectangle"""
    
    def __init__(self, width=0, height=0):
        """instantiates rectangle object with optional width & height"""
        self.height = height
        self.width = width

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
