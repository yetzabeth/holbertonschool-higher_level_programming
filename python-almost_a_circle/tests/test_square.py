#!/usr/bin/python3
"""
Unittest for class Square methods
"""
import unittest
from io import StringIO
import sys
from models.square import Square


class Test_classSquare(unittest.TestCase):

    def test_one_parameter(self):
        """ check the new instance with one argument """
        sq0 = Square(1)
        self.assertEqual(sq0.size, 1)

    def test_multiple_parameter(self):
        """ check the new instance with multiple arguments """
        sq1 = Square(1, 2)
        self.assertEqual(sq1.width, 1)
        self.assertEqual(sq1.height, 1)
        self.assertEqual(sq1.x, 2)

        sq2 = Square(1, 2, 3)
        self.assertEqual(sq2.width, 1)
        self.assertEqual(sq2.height, 1)
        self.assertEqual(sq2.x, 2)
        self.assertEqual(sq2.y, 3)

        sq3 = Square(1, 2, 3, 4)
        self.assertEqual(sq3.width, 1)
        self.assertEqual(sq3.height, 1)
        self.assertEqual(sq3.x, 2)
        self.assertEqual(sq3.y, 3)
        self.assertEqual(sq3.id, 4)

    def test_no_int_args(self):
        """ check if the arguments are not int values """
        with self.assertRaises(TypeError):
            Square("1", 2)
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_negative_size_x_y(self):
        """ check if size, x and y are a negative int """
        with self.assertRaises(ValueError):
            Square(-1, 2)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_positive_size(self):
        """ check if size is a positive int value """
        with self.assertRaises(ValueError):
            Square(0)

    def test_correct_str(self):
        """ check the correct functionality of __str__ method overrides """
        sq = Square(1, 2, 3, 4)
        self.assertEqual(sq.__str__(), '[Square] (4) 2/3 - 1')

    def test_to_dictionary(self):
        """ check the correct return of the to_dictionary method """
        sq4 = Square(1, 2, 3, 4)
        result = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(sq4.to_dictionary(), result)

    def test_update(self):
        """ check the correct update of attributes """
        sq5 = Square(1, 1, 1, 1)

        sq5.update(2)
        self.assertEqual(sq5.__str__(), '[Square] (2) 1/1 - 1')

        sq5.update(size=9, x=5, y=6)
        self.assertEqual(sq5.__str__(), '[Square] (2) 5/6 - 9')


if __name__ == "__main__":
    unittest.main()
