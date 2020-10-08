#!/usr/bin/python3
"""Create the module"""
import json


def load_from_json_file(filename):
    """Function that writes an Object to a text file"""
    with open(filename, encoding="utf-8") as myfile:
        return json.load(myfile)
