#!/usr/bin/python3

"""
Module base contain a class Base

"""
import json


class Base():
    """
    class Base definition

    Attributes:
        __nb_objects: int

    Methods:
        __init__(self, id=None)
        to_json_string(list_dictionaries)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """set id or increment id if already set """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """return JSON obj representation"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
