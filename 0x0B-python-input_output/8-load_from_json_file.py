#!/usr/bin/python3
import json
"""
8-load_from_json_file : 1 function

"""


def load_from_json_file(filename):
    """ Creates an object from a json file

        Args:
            filename (obj : 'str') name of file
    """
    with open(filename) as f:
        return json.load(f)
