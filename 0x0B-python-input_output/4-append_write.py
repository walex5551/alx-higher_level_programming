#!/usr/bin/python3

"""
4-append_write: 1 function

"""


def append_write(filename="", text=""):
    """ Append text to end of file at filename

        Args:
            filename (obj:`str`): name of file
            text (obj:`str`): text to append
    """
    with open(filename, 'a') as f:
        return f.write(text)
