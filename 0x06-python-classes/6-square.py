#!/usr/bin/python3
"""Square class"""

class Square:
    """defines a square based on size
    TypeError & ValueError exceptions are handled
    Attributes:
        __size (int): size of square class
        __position (tuple of 2 integers): position of top left element
    """
    def __init__(self, size=0, position=(0, 0)):
        """instantiation of the square object
        Args:
            size (int, optional): size of square object
            position (tuple, optional): position of top left element
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """size getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size setter
        Args:
            value (int): new size of square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position getter"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """position setter
        Args:
            value (tuple of 2 ints): coordinates
        """
        if isinstance(value, tuple) and len(value) == 2 and \
                isinstance(value[0], int) and isinstance(value[1], int) \
                and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """returns the square area based on size"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        [print() for i in range(self.__position[1])]
        if self.__size == 0:
            print()
        else:
            [print(' ' * self.__position[0] + '#' * self.__size) for i in range(self.__size)]
