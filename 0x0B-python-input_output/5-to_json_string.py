#!/usr/bin/python3
import json
"""
5-to_json_string : 1 function

"""


def to_json_string(my_obj):
    """ Returns json representation of object

        Args:
            my_obj('object'): any object
    """
    return json.dumps(my_obj)
