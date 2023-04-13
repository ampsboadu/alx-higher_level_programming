#!/usr/bin/python3
"""
Module 6-load_from_json_file

Contain a func that loads content from json file
"""


def load_from_json_file(filename):
    """load json file as obj"""
    import json

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
