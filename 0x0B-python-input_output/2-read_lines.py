#!/usr/bin/python3
"""Create a module"""


def read_lines(filename="", nb_lines=0):
    """Function that return the number of lines of the text line"""
    with open(filename, encoding="utf-8") as myfile:
        lines = myfile.readlines()
        for i, line in enumerate(lines):
            if nb_lines <= 0 or nb_lines >= len(lines):
                print(line, end="")
            elif i < nb_lines:
                print(line, end="")
