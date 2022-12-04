#!/usr/bin/python3

"""
3-write_file: 1 function

"""


def write_file(filename="", text=""):
    """ Write text to file at filename

        Args:
            filename (obj:`str`): name of file
            text (obj:`str`): text to write
    """
    with open(filename, 'w') as f:
        return f.write(text)
