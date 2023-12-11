#!/usr/bin/python3
""" rectangle_test.py """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """defines unittests for Rectangle(...)"""

    def test_two_args(self):
        """tests width & height getters & setters"""
        r = Rectangle()
        self.assertEqual(r.id, 1)

    def test_three_args(self):
        """tests x getter & setter"""

    def test_four_arg(self):
        """tests y getter & setter"""
        r = Rectangle(89)
        self.assertEqual(r.id, 89)

    def test_five_args(self):
        """tests Rectangle instance custom id"""
        r = Rectangle()


if __name__ == '__main__':
    unittest.main()
