#!/usr/bin/python3
"""Create a module"""


def number_of_lines(filename=""):
    """Function that return the number of lines of the text line"""
    with open("my_file_0.txt", encoding="utf-8") as myfile:
            line = len(myfile.readlines())
    return line
