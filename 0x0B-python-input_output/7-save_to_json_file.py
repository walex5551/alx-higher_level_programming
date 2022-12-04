#!/usr/bin/python3
import json
"""
7-save_to_json_file : 1 function

"""


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file in json representation

        Args:
            my_obj ('object'): object to save
            filename (obj : 'str') name of file
    """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
