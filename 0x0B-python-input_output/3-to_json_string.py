#!/usr/bin/python3
"""
Module 3-to_json_string

Contain a function that convert str to json
"""


def to_json_string(my_obj):
    """return json from string"""
    import json

    return json.dumps(my_obj)
