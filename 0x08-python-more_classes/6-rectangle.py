#!/usr/bin/python3

"""
Module 3-rectangle
contains class Rectangle
attributes height and width both Integers values
"""


class Rectangle():
    """
    class Rectangle definition

    Attributes:
        width: int
        height: int
        number_of_instances: int [Number Rectangle instances created]

    Methods:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __strr__(self)
        __repr__(self)
        __del__(self)
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initialize new Rectangle """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ return width of rectangle """
        return self. __width

    @width.setter
    def width(self, value):
        """ set new value to width. value must int greater than 0 """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ return height of rectangle """
        return self. __height

    @height.setter
    def height(self, value):
        """ set new value to height. value must int greater than 0 """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ return area (width * height) of rectangles """
        return self.__width * self.__height

    def perimeter(self):
        """ return perimeter (2widths + 2heights) of rectangles """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ draws rectangle with #pixels """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rec

    def __repr__(self):
        """ return string representation of instances created """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ deletes rectangle instance """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
