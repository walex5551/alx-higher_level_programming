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
from models.square import Square
from models.rectangle import Rectangle


class test_Square(unittest.TestCase):
    """ Tests functionality of class Square """

    def setUp(self):
        """ setUp deletes Square.json if it exists,
        resets nb_objects to 0, and creates a new rectangle
        """
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        Base.nbreset()
        self.rect = Square(1, 2, 1, 2)

    def test_Square(self):
        """ Test square functionality and type """
        with self.assertRaises(TypeError):
            sq = Square()

        sq = Square(1, 3, 4)

        self.assertEqual(sq.height, 1)

        self.assertEqual(sq.width, 1)

        self.assertEqual(sq.id, 1)

        self.assertTrue(isinstance(sq, Base))

        self.assertTrue(issubclass(Square, Base))

        self.assertFalse(isinstance(Square, Base))

        self.assertTrue(isinstance(sq, Rectangle))

        self.assertTrue(issubclass(Square, Rectangle))

        self.assertFalse(isinstance(Square, Rectangle))

    def test_str(self):
        """ Test string functionality """
        sq = Square(1, 2, 3, 4)
        self.assertEqual(str(sq), "[Square] (4) 2/3 - 1")

    def test_size(self):
        """ Test size functionality """
        sq = Square(1)
        self.assertEqual(sq.size, 1)

        sq = Square(3, 4, 5, 6)
        self.assertEqual(sq.size, 3)

        with self.assertRaises(ValueError):
            sq = Square(0, 2)

        with self.assertRaises(ValueError):
            sq = Square(1, 2, -4, 8)

    def test_input(self):
        """ Test input variations """
        with self.assertRaises(TypeError):
            r = Square()

        with self.assertRaises(TypeError):
            r = Square(1, 2, 3, 4, 5, 6, 7)

        r = Square(4, 8, 1, 2)
        self.assertTrue(isinstance(r, Base))

        self.assertFalse(isinstance(Square, Base))

        self.assertTrue(issubclass(Square, Base))

    def test_area(self):
        """ Area functionality """
        sq = Square(4, 4)
        self.assertEqual(sq.area(), 16)

        sq = Square(2, 2, 0, 0)
        self.assertEqual(sq.area(), 4)

        with self.assertRaises(ValueError):
            sq = Square(0, 0)
            self.assertEqual(sq.area(), 0)

    def test_display(self):
        """Modify offset functionality """
        r = Square(1, 1, 0, 0)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            res = f.getvalue()
        self.assertEqual(res, " #\n")

        r = Square(1, 1, 2, 0)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            res = f.getvalue()
        self.assertEqual(res, "\n\n #\n")

        r = Square(1, 1, 0, 2)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            res = f.getvalue()
        self.assertEqual(res, " #\n")

        r = Square(1, 1, 2, 2)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            res = f.getvalue()
        self.assertEqual(res, "\n\n #\n")

    def test_update(self):
        """ Test update functionality """
        sq = Square(1)

        with self.assertRaises(TypeError):
            sq.update(2, 3, 4, "str")

        with self.assertRaises(ValueError):
            sq.update(1, 0, 4)

        with self.assertRaises(ValueError):
            sq.update(1, 2, 4, -8)

        with self.assertRaises(ValueError):
            sq.update(1, 2, -4, 8)

    def test_file(self):
        """ Test creating, saving, modifying files """
        d = Square.to_json_string([self.rect.to_dictionary()])
        self.assertIsInstance(d, str)

        d = Square.to_json_string([self.rect.to_dictionary()])
        self.assertEqual(json.loads(d), [self.rect.to_dictionary()])

        d = Square.to_json_string([])
        self.assertEqual(d, "[]")

        d = Square.to_json_string(None)
        self.assertEqual(d, "[]")

        r = Square(2, 2, 2, 2)
        Square.save_to_file([self.rect, r])
        with open("Square.json") as f:
            self.assertEqual(len(json.load(f)), 2)

        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(len(json.load(f)), 0)

        with self.assertRaises(AttributeError):
            Square.save_to_file("str")

        with self.assertRaises(TypeError):
            d = Square.from_json_string(TypeError)

        with self.assertRaises(ValueError):
            d = Square.from_json_string("bad")

    def test_to_dict(self):
        """ Test to_dict functionality """
        sq_dict = {'x': 1, 'y': 2, 'height': 3, 'width': 4}
        sq1 = Square(1, 2, 3, 4)
        sq1_dict = sq1.to_dictionary()
        self.assertEqual(len(sq_dict), len(sq1_dict))

        sq2 = Square(1, 2)
        sq2.update(**sq1_dict)
        sq2_dict = sq2.to_dictionary()
        self.assertEqual(len(sq1_dict), len(sq2_dict))
        self.assertEqual(type(sq2_dict), dict)
        self.assertFalse(sq1 == sq2)

        with self.assertRaises(TypeError):
            sq = Square(1, 2, 3, 4)
            sq_dict = sq1.to_dictionary("str")

if __name__ == '__main__':
    unittest.main()
