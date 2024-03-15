#!/usr/bin/python3
""" update_test.py """
import unittest


class TestUpdate(unittest.TestCase):
    """defines unittests for update() method"""

    def test_no_args(self):
        """tests update() for Rectangles & Squares"""

    def test_args(self):
        """tests update(*args) method for Rectangles & Squares"""

    def test_args_kwargs(self):
        """tests update(*args, **kwargs) method for Rectangles & Squares"""

    def test_kwargs(self):
        """tests update(**kwargs) method for Rectangles & Squares"""


if __name__ == '__main__':
    unittest.main()
