#!/usr/bin/python3
"""Create a module"""


def write_file(filename="", text=""):
    """Function that return the number of lines of the text line"""
    with open(filename, 'w', encoding="utf-8") as myfile:
        return myfile.write(text)
