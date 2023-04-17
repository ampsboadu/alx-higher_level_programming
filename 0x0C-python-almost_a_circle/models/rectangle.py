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
        width(self): width getter
        width(self, value): width setter
        height(self): height getter
        height(self, value): height setter
        x(self): x getter
        x(self, value): x setter
        y(self): y getter
        y(self, value): y setter
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter. value must be int greater than 0"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter. value must int greater than 0 """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter. value must int greater than 0 """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter. value must int greater than 0 """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value
