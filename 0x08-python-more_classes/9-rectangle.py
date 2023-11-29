#!/usr/bin/python3
"""
9-rectangle.py
"""


class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """instantiates rectangle object with optional width & height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """returns a string representation of rectangle object
        with character #"""
        if self.height == 0 or self.width == 0:
            return ('')
        return (f'{self.print_symbol}' * self.width + '\n') \
            * (self.height - 1) + f'{self.print_symbol}' * self.width

    def __repr__(self):
        """returns a string representation to recreate
        a new instance with eval()"""
        return (f'Rectangle({self.width:d}, {self.height:d})')

    def __del__(self):
        """prints when a rectangle object is deleted"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return (cls(size, size))
