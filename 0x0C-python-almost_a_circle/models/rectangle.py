#!/usr/bin/python3
"""
Module rectangle
contains class Rectangle which inherits from Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    class Rectangle definition

    Attributes:
        width: int
        height: int
        x: int
        y: int
        id: int (inherited)

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): init new obj
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
