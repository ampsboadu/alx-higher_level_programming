#!/usr/bin/python3
"""
Module 2-append_write

COntains a function that append text to file
"""


def append_write(filename="", text=""):
    """append text to file and return char count """
    with open(filename, 'a', encoding='utf-8') as f:
        return(f.write(text))
