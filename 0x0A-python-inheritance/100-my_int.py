#!/usr/bin/python3
"""
100-my_int.py
"""


class MyInt(int):
    """inherits from 'int'
    (rebel class) => switches '==' & '!=' operators"""

    def __eq__(self, other):
        """returns True if not equal, otherwise False"""
        return (super().__ne__(other))

    def __ne__(self, other):
        """returns True if equal, otherwise False"""
        return (super().__eq__(other))
