#!/usr/bin/python3
"""
12-student : 1 class

"""


class Student:
    """ New class student

        Attributes:
            first_name (obj : 'str') : first name
            last_name (obj : 'str') : last name
            age (obj : 'int') : age
    """

    def __init__(self, first_name, last_name, age):
        """ Initializing attributes """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Makes dictionary representation of class for json

            Args:
                self(class) : refers to student
                attrs(obj : 'str') : list of attributes (strings)

        """

        if type(attrs) is not list:
            return self.__dict__
        for attribute in attrs:
            if type(attribute) is not str:
                return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}
