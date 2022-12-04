#!/usr/bin/python3
import json
"""
6-from_json_string : 1 function

"""


def from_json_string(my_str):
    """ Returns json representation of string

        Args:
            my_str(obj : 'string'): json string
    """
    return json.loads(my_str)
