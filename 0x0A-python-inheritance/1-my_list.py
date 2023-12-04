#!/usr/bin/python3
"""
1-my_list.py
"""


class MyList(list):
    """inherits from 'list' a public instance method (print_sorted)"""

    def print_sorted(self):
        """printd a list, but sorted (ascending order)"""
        print(sorted(self))
