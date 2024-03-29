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
        area(self): calculate and return area of Rectangle instance
        display(self): print stdout the Rectangle instance with #
        __str__(self): return str representation of Rectangle instance
        update(self, *args): updates attributes of Rectangle instance
        to_dictionary(self): returns dict rep of Rectangle instance
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
        elif value <= 0:
            raise ValueError('width must be > 0')
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
        elif value <= 0:
            raise ValueError('height must be > 0')
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

    def area(self):
        """return area of Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """draws rectangle with #pixels"""
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for i in range(self.__height)))

    def __str__(self):
        """string representation of Rectangle instance"""
        str1 = f"[{self.__class__.__name__}] ({self.id}) {self.__x}/"
        str2 = f"{self.__y} - {self.__width}/{self.__height}"
        return str1 + str2

    def update(self, *args, **kwargs):
        """updates attributes of Rectangle instance with args"""
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.width = j
                elif i == 2:
                    self.height = j
                elif i == 3:
                    self.x = j
                else:
                    self.y = j
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """return dic representation of Rectangle instance"""
        dic = {}
        dic['id'] = self.id
        dic['width'] = self.width
        dic['height'] = self.height
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
