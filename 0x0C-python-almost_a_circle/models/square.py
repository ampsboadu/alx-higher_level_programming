#!/usr/bin/python3
"""
Module square
contains class Square which inherits from Rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square definition

    Attributes:
        size: int
        width: int (Inherited)
        height: int (Inherited)
        x: int (inherited)
        y: int (inherited)

    Methods:
        __init__(self, size, x=0, y=0, id=None): inits new obj
        size(self): size getter
        size(self, value): size setter
        __str__(self): return str representation of Square instance

    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize new instance"""
        super().__init__(size, size, x, y)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of Square instance"""
        str1 = f"[{self.__class__.__name__}] ({self.id}) {self.x}/"
        str2 = f"{self.y} - {self.size}"
        return str1 + str2
