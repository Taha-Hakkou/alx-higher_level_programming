#!/usr/bin/python3
"""
10-square.py
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""

    def __init__(self, size):
        """instantiates square object with size"""
        try:
            self.integer_validator("size", size)
            self.__size = size
            super().__init__(size, size)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

    def area(self):
        """returns the area of square object"""
        return (self.__size ** 2)
