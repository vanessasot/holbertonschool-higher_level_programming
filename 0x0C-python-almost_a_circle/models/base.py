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

    @staticmethod
    def from_json_string(json_string):
        """String representation of JSON"""
        if json_string:
            return json.loads(json_string)
        else:
            newlist = []
            return newlist

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            value = cls(2, 7)
        elif cls.__name__ == "Square":
            value = cls(4)
        value.update(**dictionary)
        return value

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        insta_file = "{}.json".format(cls.__name__)
        try:
            list_insta = []
            with open(insta_file, encoding="utf-8") as my_file:
                read = Base.from_json_string(my_file.read())
                for dic in read:
                    list_insta.append(cls.create(**dic))
                return list_insta
        except IOError:
            return []
