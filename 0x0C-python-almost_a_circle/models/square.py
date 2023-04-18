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
        update(self, *args, **kwargs): updates attributes of Square instance
        to_dictionary(self): return dict rep of Square instance
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

    def update(self, *args, **kwargs):

        """updates attrs of Square instance with args & kwargs"""
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                else:
                    self.y = j
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """return dic representation of Square instance"""
        dic = {}
        dic['id'] = self.id
        dic['size'] = self.size
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
