#!/usr/bin/python3
""" square_test.py """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """defines unittests for Square(...)"""

    def test_one_arg(self):
        """tests Square instance getter & setter"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_more_args(self):
        """tests Square instance custom coordinates & id"""
        b1, b2, b3 = Base(), Base(98), Base()
        self.assertEqual(b3.id, 2)


if __name__ == '__main__':
    unittest.main()
