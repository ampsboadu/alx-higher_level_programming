#!/usr/bin/python3
"""
Module 4-from_json_string

Contains a function that converts json to str
"""


def from_json_string(my_str):
    """return str rep from json"""
    import json

    return json.loads(my_str)
