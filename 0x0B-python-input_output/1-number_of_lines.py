#!/usr/bin/python3
"""
1-number_of_lines : 1 function

"""


def number_of_lines(filename=""):
    """ Return number of lines in the read file

        Args:
            filename(obj : 'str'): name of file
    """
    with open(filename) as f:
        return len(f.readlines())
