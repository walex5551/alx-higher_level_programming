#!/usr/bin/python3
"""
100-append_after - 1 function

"""


def append_after(filename="", search_string="", new_string=""):
    """ Print text preceding a line with an instance of search_string

        Args:
            filename(obj : 'str'): name of file
            search_string(obj : 'str) string to find in line
            new_string(obj : 'str') string to add

    """
    with open(filename) as f:
        lines = f.readlines()

    with open(filename, "w") as fw:
        l = ""
        for line in lines:
            l += line
            if search_string in line:
                l += new_string
        fw.write(l)
