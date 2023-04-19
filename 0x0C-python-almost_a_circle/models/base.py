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
        __init__(self, id=None):
        to_json_string(list_dictionaries):
        save_to_file(cls, list_objs):
        from_json_string(json_string):
        create(cls, **dictionary):
        load_from_file(cls):
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """set id or increment id if already set """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON obj representation"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string rep of objs to file"""
        objs = []
        if list_objs is not None:
            for i in list_objs:
                objs.append(cls.to_dictionary(i))

        with open(cls.__name__ + ".json", 'w') as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string rep"""
        if json_string is None or len(json_string) == 0:
            json_string = '[]'
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from file"""
        lst = []
        try:
            with open(cls.__name__ + ".json", 'r') as f:
                ins = cls.from_json_string(f.read())
            for i, j in enumerate(ins):
                lst.append(cls.create(**ins[i]))
        except:
            pass
        return lst
