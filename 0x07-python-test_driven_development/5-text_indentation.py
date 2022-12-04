#!/usr/bin/python3
"""
This function contains text_indentation
"""

def text_indentation(text):
    """
    Args:
        text: string to parse
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(". ", ".\n\n").replace("? ", "?\n\n")\
                        .replace(": ", ":\n\n")
    strings = text.splitlines(keepends=True)
    ret = ""
    for words in strings:
        ret += words.strip(" ")
    print(ret, end="")
