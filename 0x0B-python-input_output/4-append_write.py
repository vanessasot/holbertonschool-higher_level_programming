#!/usr/bin/python3
"""Create a module"""


def append_write(filename="", text=""):
    """Function that return the number of lines of the text line"""
    with open(filename, 'a', encoding="utf-8") as myfile:
        return myfile.write(text)
