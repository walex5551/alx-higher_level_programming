#!/usr/bin/python3
"""
unittest module for rectangle subclass

"""
import unittest
import json
import os
import sys
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class test_Rectangle(unittest.TestCase):
    """ Tests functionality of class Rectangle """

    def setUp(self):
        """ setUp deletes Rectangle.json if it exists,
        resets nb_objects to 0, and creates a new rectangle
        """
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        Base.nbreset()
        self.rect = Rectangle(1, 2, 1, 2)

    def test_input(self):
        """ Test input variations """
        with self.assertRaises(TypeError):
            r = Rectangle()

        with self.assertRaises(TypeError):
            r = Rectangle(1)

        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6, 7)

        r = Rectangle(4, 8, 1, 2)
        self.assertTrue(isinstance(r, Base))

        self.assertFalse(isinstance(Rectangle, Base))

        self.assertTrue(issubclass(Rectangle, Base))

    def test_str(self):
        """ String functionality """

        r = Rectangle(1, 2, 3, 4, 5)
        res = str(r)
        self.assertEqual(
            res, '[Rectangle] (5) 3/4 - 1/2')

    def test_area(self):
        """ Area functionality """
        r = Rectangle(4, 4)
        self.assertEqual(r.area(), 16)

        r1 = Rectangle(2, 2, 0, 0)
        self.assertEqual(r1.area(), 4)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 0)
            self.assertEqual(r.area(), 0)

    def test_display(self):
        """Modify offset functionality """
        r = Rectangle(1, 1, 0, 0)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            res = f.getvalue()
        self.assertEqual(res, "#\n")

        r = Rectangle(1, 1, 2, 0)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            res = f.getvalue()
        self.assertEqual(res, "  #\n")

        r = Rectangle(1, 1, 0, 2)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            res = f.getvalue()
        self.assertEqual(res, "\n\n#\n")

        r = Rectangle(1, 1, 2, 2)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            res = f.getvalue()
        self.assertEqual(res, "\n\n  #\n")

    def test_file(self):
        """ Test creating, saving, modifying files """
        d = Rectangle.to_json_string([self.rect.to_dictionary()])
        self.assertIsInstance(d, str)

        d = Rectangle.to_json_string([self.rect.to_dictionary()])
        self.assertEqual(json.loads(d), [self.rect.to_dictionary()])

        d = Rectangle.to_json_string([])
        self.assertEqual(d, "[]")

        d = Rectangle.to_json_string(None)
        self.assertEqual(d, "[]")

        r = Rectangle(2, 2, 2, 2)
        Rectangle.save_to_file([self.rect, r])
        with open("Rectangle.json") as f:
            self.assertEqual(len(json.load(f)), 2)

        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(len(json.load(f)), 0)

        with self.assertRaises(AttributeError):
            Rectangle.save_to_file("str")

        with self.assertRaises(TypeError):
            d = Rectangle.from_json_string(TypeError)

        with self.assertRaises(ValueError):
            d = Rectangle.from_json_string("bad")

    def test_to_dict(self):
        """ Test to_dict functionality """
        r1 = Rectangle(1, 2, 3, 4)
        r1_dictionary = r1.to_dictionary()
        r_dictionary = {'x': 1, 'y': 2, 'id': 1, 'height': 3, 'width': 4}
        self.assertEqual(len(r1_dictionary), len(r_dictionary))
        self.assertEqual(type(r1_dictionary), dict)

        r2 = Rectangle(1, 2)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(len(r1_dictionary), len(r2_dictionary))
        self.assertEqual(type(r2_dictionary), dict)
        self.assertFalse(r1 == r2)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4)
            r1_dictionary = r1.to_dictionary("Hi")

    def test_update(self):
        """ Update value functionality """
        with self.assertRaises(TypeError):
            self.rect.update(1, "str")

        self.rect.update(6, 6, 6, 6, 6, 6)

        self.rect.update(3, 3, 3, 3, 3)

        self.assertEqual(self.rect.width, 3)

        self.assertEqual(self.rect.height, 3)

        self.assertEqual(self.rect.x, 3)

        self.assertEqual(self.rect.y, 3)

        self.assertEqual(self.rect.id, 3)

        d = self.rect.to_dictionary()
        self.rect.update(id="str", width=1, x=1)
        d1 = self.rect.to_dictionary()
        self.assertNotEqual(d, d1)

        d1 = self.rect.to_dictionary()
        self.rect.update(rand=5)


class test_validator(unittest.TestCase):
    """ Test int validator """
    def setUp(self):
        """ Reset nb_objects and create an empty rectangle """
        Base.nbreset()
        self.rect = Rectangle(1, 1, 1, 1)

    def test_x(self):
        """ check x dimension """
        self.assertEqual(self.rect.x, 1)

        self.rect.x = 2
        self.assertEqual(self.rect.x, 2)

        with self.assertRaises(TypeError):
            self.rect.x = None

        with self.assertRaises(ValueError):
            self.rect.x = -2

        self.assertEqual(self.rect.y, 1)

    def test_y(self):
        """ Check y dimension """
        self.rect.y = 2
        self.assertEqual(self.rect.y, 2)

        with self.assertRaises(TypeError):
            self.rect.y = None

        with self.assertRaises(ValueError):
            self.rect.y = -2

    def test_width(self):
        """ Check width dimension """
        self.assertEqual(self.rect.width, 1)

        self.rect.width = 2
        self.assertEqual(self.rect.width, 2)

        with self.assertRaises(TypeError):
            self.rect.width = None

        with self.assertRaises(ValueError):
            self.rect.width = -2

    def test_height(self):
        """ Check height dimension """
        self.assertEqual(self.rect.height, 1)

        self.rect.height = 2
        self.assertEqual(self.rect.height, 2)

        with self.assertRaises(TypeError):
            self.rect.height = None

        with self.assertRaises(ValueError):
            self.rect.height = -2

if __name__ == '__main__':
    unittest.main()
