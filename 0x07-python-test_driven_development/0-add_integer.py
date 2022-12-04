#!/usr/bin/python3
"""
This function contains add_integer
"""

def add_integer(a, b=98):
    """
    Args:
        a: int
        b: int
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
