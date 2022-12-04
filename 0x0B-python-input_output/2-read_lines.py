#!/usr/bin/python3
"""
2-read_lines : 1 function

"""


def read_lines(filename="", nb_lines=0):
    """ Return number of lines in the read file

        Args:
            filename(obj : 'str'): name of file
            nb_lines(obj : 'int'): number of lines to read
    """
    with open(filename) as f:
        i = len(list(f))
        if nb_lines >= i or nb_lines <= 0:
            nb_lines = i
        f.seek(0, 0)
        for i in range(nb_lines):
            print(f.readline(), end="")
