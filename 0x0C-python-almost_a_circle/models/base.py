#!/usr/bin/python3
"""Create the module"""
import json


class Base:
    """Create the first class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the representation of string JSON"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Write string representation JSON"""
        j_file = "{}.json".format(cls.__name__)
        if list_objs is None:
            newdictionary = []
        else:
            newdictionary = [item.to_dictionary() for item in list_objs]
        with open(j_file, "w", encoding="utf-8") as j_file:
            j_file.write(cls.to_json_string(newdictionary))
