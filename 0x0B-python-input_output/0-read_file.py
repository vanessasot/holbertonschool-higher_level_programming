#!/usr/bin/python3
"""Create a module"""


def read_file(filename=""):
    """Function that read a text file and print in stdout"""
    with open("my_file_0.txt") as i:
        for line in i:
            print(line, end="")
