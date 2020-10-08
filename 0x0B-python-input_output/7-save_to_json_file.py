#!/usr/bin/python3
"""Create the module"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file"""
    with open(filename, 'w', encoding="utf-8") as myfile:
        return json.dump(my_obj, myfile)
