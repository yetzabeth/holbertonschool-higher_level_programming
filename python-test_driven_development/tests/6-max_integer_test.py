#!/usr/bin/python3
"""unittests for the function
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_all(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([1, 2, -3]), 2)
        self.assertEqual(max_integer([5, 4]), 5)
        self.assertEqual(max_integer([3, 5, 2]), 5)
