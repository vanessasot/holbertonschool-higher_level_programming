#!/usr/bin/python3
"""Create the module"""


def inherits_from(obj, a_class):
    """Define the function"""
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
