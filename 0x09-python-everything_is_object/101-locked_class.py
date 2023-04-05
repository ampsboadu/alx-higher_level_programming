#!/usr/bin/python3
"""
Module 101-locked_class
Restricts creating of attributes
"""


class LockedClass:
    """
    Only create instance attribute if its 'first_name'
    """

    __slot__ = "first_name"
