#!/usr/bin/python3
class MagicClass:
    """magic class (Python bytecode)
    Attributes:
        _MagicClass__radius (int or float): radius of MagicClass class"""
    def __init__(self, radius):
        """instantiates the MagicClass object
        Args:
            radius (int or float): radius of MagicClass object"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """returns the area of MagicClass object"""
        return ((self._MagicClass__radius ** 2) * math.pi)

    def circumference(self):
        """returns the circumference of MagicClass object"""
        return (2 * math.pi * self._MagicClass__radius)
