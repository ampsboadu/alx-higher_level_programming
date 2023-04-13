#!/usr/bin/python3
"""
Module 0-read_file

Contains a function that read file and print content
"""


def read_file(filename=""):
    """ Read file and print content """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
