#!/usr/bin/python3
"""
1-base.py - 1 class
"""
import json


class Base:
    """ Define base for rectangle and square classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize and increment amount of objects """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def nbreset(cls):
        """ Reset number of objects """
        cls.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Make a json str out of input dict """
        if list_dictionaries is None or []:
            return "[]"
        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Make/save a json string to a file """
        if list_objs is None:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        with open(cls.__name__ + ".json", "w") as fp:
            fp.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """ Load a string from a json file """
        if json_string is None or json_string is "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create dict """
        if cls.__name__ == 'Rectangle':
            o = cls(3, 3)
        elif cls.__name__ == 'Square':
            o = cls(1)
        o.update(**dictionary)
        return o

    @classmethod
    def load_from_file(cls):
        """ Load a json string from a file and return dictionary """
        try:
            with open(cls.__name__ + ".json", 'r') as fp:
                pass
        except FileNotFoundError:
            return []
        with open(cls.__name__ + ".json", 'r') as fp:
            load = cls.from_json_string(fp.read())
            return [cls.create(**d) for d in load]
