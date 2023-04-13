#!/usr/bin/python3
"""
Module 8-class_to_json

Contains a func that return dict of class obj
"""


def class_to_json(obj):
    """returns dict description of class obj"""
    return obj.__dict__
