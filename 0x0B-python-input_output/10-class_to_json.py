#!/usr/bin/python3
"""
10-class_to_json : 1 function

"""


def class_to_json(obj):
    """ Return dict description of a class instance

        Args:
            obj ('object'): any object
    """
    return obj.__dict__
