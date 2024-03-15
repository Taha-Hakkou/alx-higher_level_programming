#!/usr/bin/python3
""" base_test.py """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """defines unittests for Base(...)"""

    def test_no_args(self):
        """tests Base instance default id"""
        b = Base()
        self.assertEqual(b.id, 1)
        del b

    def test_one_arg(self):
        """tests Base instance custom id"""
        b = Base(89)
        self.assertEqual(b.id, 89)
        del b

    def test_id_inc(self):
        """tests Base instances id affectation flow"""
        b1, b2, b3 = Base(), Base(98), Base()
        self.assertEqual(b3.id, 2)
        del b1
        del b2
        del b3


if __name__ == '__main__':
    unittest.main()
