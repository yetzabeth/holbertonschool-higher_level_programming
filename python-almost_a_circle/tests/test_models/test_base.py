#!/usr/bin/python3
"""
Unittest for class Base methods
"""
import unittest
from models.base import Base


class Test_classBase(unittest.TestCase):

    def test_auto_id(self):
        """ to check the auto-assignement of an id value """
        base0 = Base(id=None)
        self.assertEqual(base0.id, 1)

        base1 = Base()
        self.assertEqual(base1.id, 2)

    def test_negative_id(self):
        """ to check the assignement of an id negative value """
        base2 = Base(-10)
        self.assertEqual(base2.id, -10)

    def test_strign_id(self):
        """ to check the assignement of an id string value """
        base4 = Base("string")
        self.assertEqual(base4.id, "string")

    def test_float_id(self):
        """ to check the assignement of an id float value """
        base5 = Base(3.14)
        self.assertEqual(base5.id, 3.14)

    def test_list_id(self):
        """ to check the assignement of an id list value """
        base6 = Base(['love', 'buzz'])
        self.assertEqual(base6.id, ['love', 'buzz'])

    def test_math_id(self):
        """ to check the assignement of an id value by math operation"""
        base7 = Base(7**2)
        self.assertEqual(base7.id, 49)

    def test_big_id(self):
        """ to check the assignement of an id big number value """
        base8 = Base(1e09)
        self.assertEqual(base8.id, 1e09)

    def test_multiple_args(self):
        """ to check the correct qty of arguments """
        with self.assertRaises(TypeError):
            Base(2, 4, 5, 8)

    def test_toJSONstring_data(self):
        """ check method with a non empty list as argument """
        list_dict = [{'x':0}, {'x':2}]
        self.assertEqual(Base.to_json_string(list_dict),'[{"x": 0}, {"x": 2}]')

        """ check method without any argument """
        self.assertEqual(Base.to_json_string(None), '[]')

        """ check method with an empty list as argument """
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_fromJSONstring(self):
        """ check method without any argument """
        self.assertEqual(Base.from_json_string(None), [])

        """ check method with an empty list as argument """
        self.assertEqual(Base.from_json_string("[]"), [])

        """ check method with a non empty list as argument """
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])

if __name__ == "__main__":
    unittest.main()
