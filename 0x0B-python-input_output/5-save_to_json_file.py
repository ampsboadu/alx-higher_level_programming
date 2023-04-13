#!/usr/bin/python3
"""
Module 5-save_to_json_file

Contains a func that writes obj to text file with JSON rep
"""


def save_to_json_file(my_obj, filename):
    """writes obj to text file using JSON rep """
    import json

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
