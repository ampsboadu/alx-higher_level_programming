#!/usr/bin/python3
"""
Module 1-write_file

Contain a function that write text to file
"""


def write_file(filename="", text=""):
    """ writes text to file and return char count """
    with open(filename, 'w', encoding='utf-8') as f:
        return(f.write(text))
