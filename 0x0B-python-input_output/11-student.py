#!/usr/bin/python3
"""
11-student : 1 class

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

    def to_json(self):
        return self.__dict__
