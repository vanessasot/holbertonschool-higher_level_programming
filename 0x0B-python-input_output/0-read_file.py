#!/usr/bin/python3
"""Create a module"""


def read_file(filename=""):
    """Function that read a text file and print in stdout"""
    with open(filename, encoding="utf-8") as myfile:
        for line in myfile:
            print(line, end="")
