#!/usr/bin/python3
"""Create a module"""


def number_of_lines(filename=""):
    """Function that return the number of lines of the text line"""
    line_number = 0
    with open("my_file_0.txt") as myfile:
        for line in myfile:
            line_number += 1
        return line_number
