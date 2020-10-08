#!/usr/bin/python3
"""Create the module"""
import json


def from_json_string(my_str):
    """Function that returns the JSON representation of an object (string)"""
    my_obj = json.loads(my_str)
    return my_obj
