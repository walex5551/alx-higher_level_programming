#!/usr/bin/python3
"""
This function contains print_square
"""

def print_square(size):
    """
    Args:
        size: size of square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
