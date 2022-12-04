#!/usr/bin/python3
""" Tests for base and base functions """

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_base(unittest.TestCase):
    """ Test for Base class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test id functionality """

        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base(4)
        self.assertEqual(b.id, 4)
        b = Base(0)
        self.assertEqual(b.id, 0)
        b = Base(333)
        self.assertEqual(b.id, 333)
        b = Base(-2)
        self.assertEqual(b.id, -2)

    def test_type(self):
        """ Test type and instance """

        b = Base()
        self.assertEqual(type(b), Base)
        self.assertTrue(isinstance(b, Base))

    def test_to_json_string(self):
        """ Test to_json_string functionality """

        d = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        json_d = Base.to_json_string([d])

        self.assertTrue(isinstance(d, dict))

        self.assertTrue(isinstance(json_d, str))

        self.assertCountEqual(
            json_d, '{["id": 1, "x": 2, "y": 3, "width": 4, "height": 5]}')

        json_d = Base.to_json_string([])
        self.assertEqual(json_d, "[]")

        json_d_1 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")

        err = ("to_json_string() missing 1 required positional argument: " +
               "'list_dictionaries'")
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        self.assertEqual(err, str(e.exception))

        err = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(err, str(e.exception))

        with self.assertRaises(TypeError) as e:
            Base.to_json_string("str")
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                e.exception))

        with self.assertRaises(TypeError) as e:
            Base.to_json_string(["list", "strings"])
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                e.exception))

        with self.assertRaises(TypeError) as e:
            Base.to_json_string(1.2)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                e.exception))

        with self.assertRaises(TypeError) as e:
            Base.to_json_string([1, 2, 3, 4])
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                e.exception))

        with self.assertRaises(TypeError) as e:
            Base.to_json_string({1: 'dict', 2: 'value'})
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                e.exception))

        with self.assertRaises(TypeError) as e:
            Base.to_json_string((0, 0))
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                e.exception))

    def test_save_to_file(self):
        """Test class method save_to_file with normal types."""
        with self.assertRaises(AttributeError) as e:
            Base.save_to_file([Base(1), Base(2)])
        self.assertEqual(
             "'Base' object has no attribute 'to_dictionary'", str(
                e.exception))

        with self.assertRaises(AttributeError) as e:
            Rectangle.save_to_file([1, 2])
        self.assertEqual(
            "'int' object has no attribute 'to_dictionary'", str(
                e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file(2)
        self.assertEqual(
            "'int' object is not iterable", str(
                e.exception))
        err = ("save_to_file() missing 1 required" +
               " positional argument: 'list_objs'")

        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file()
        self.assertEqual(err, str(e.exception))

    def test_from_json_string(self):
        """ Test from_json_string functionality """

        err = ("from_json_string() missing 1" +
               " required positional argument: 'json_string'")
        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string()
        self.assertEqual(err, str(e.exception))

        er = "from_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string("str", 5)
        self.assertEqual(er, str(e.exception))

        list_in = [
            {'id': 2, 'width': 2, 'height': 4},
            {'id': 5, 'width': 3, 'height': 6}
        ]
        json_in = Rectangle.to_json_string(list_in)
        json_out = Rectangle.from_json_string(json_in)
        self.assertEqual(type(json_out), list)

        with self.assertRaises(TypeError) as e:
            l = Rectangle.from_json_string([1, 2])
        self.assertEqual("the JSON object must be str, not 'list'",
                         str(e.exception))

        with self.assertRaises(TypeError) as e:
            l = Rectangle.from_json_string(1)
        self.assertEqual("the JSON object must be str, not 'int'",
                         str(e.exception))

        with self.assertRaises(TypeError) as e:
            l = Rectangle.from_json_string(1.2)
        self.assertEqual("the JSON object must be str, not 'float'",
                         str(e.exception))

        with self.assertRaises(TypeError) as e:
            l = Rectangle.from_json_string((8, 9))
        self.assertEqual("the JSON object must be str, not 'tuple'",
                         str(e.exception))

        with self.assertRaises(TypeError) as e:
            l = Rectangle.from_json_string({1: 'value', 2: 'dict'})
        self.assertEqual("the JSON object must be str, not 'dict'",
                         str(e.exception))

    def test_create(self):
        """ Test create functionality """
        with self.assertRaises(TypeError) as e:
            err = Rectangle.create("str")
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given", str(
                e.exception))

    def test_load_from_file(self):
        """Test load_from_file functionality """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        if os.path.exists("Base.json"):
            os.remove("Base.json")

        r_output = Rectangle.load_from_file()
        self.assertEqual(r_output, [])

        sq_output = Square.load_from_file()
        self.assertEqual(sq_output, [])

        er = "load_from_file() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            list_rectangles_output = Rectangle.load_from_file("str")
        self.assertEqual(er, str(e.exception))

if __name__ == '__main__':
    unittest.main()
