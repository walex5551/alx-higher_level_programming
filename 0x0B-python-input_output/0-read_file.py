#!/usr/bin/python3
"""
0-read_file : 1 function

"""


def read_file(filename=""):
    """ Read from a file

        Args:
            filename(obj : 'str'): name of file
    """
    with open(filename) as f:
        print(f.read(), end="")
