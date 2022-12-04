#!/usr/bin/python3

"""
This function contains say_my_name
"""

def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: string 1
        last_name: string 2
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
