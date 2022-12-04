#!/usr/bin/python3
"""
rectangle.py : 1 class

"""
from models.base import Base


class Rectangle(Base):
    """ Inherits attributes from Base
        Attributes:
            width (obj:`int`): width of the rectangle
            height (obj:`int`): height of the rectangle
            x (obj:`int`): x offset of the rectangle
            y (obj:`int`): y offset of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """ String representation of the Rectangle """
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def int_validator(self, key, value):
        """ Raise Errors if incorrect input

            Args:
                key: name of the attribute
                value: value of the attribute
        """
        if type(value) is not int:
            raise TypeError(key + " must be an integer")
        elif key is "width" or key is "height":
            if value <= 0:
                raise ValueError(key + " must be > 0")
        elif key is "x" or key is "y":
            if value < 0:
                raise ValueError(key + " must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.int_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.int_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.int_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.int_validator("y", value)
        self.__y = value

    def area(self):
        """ Return area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle in "#"s """
        if self.__y > 0:
            print("\n" * (self.__y), end="")
        for x in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """ Update values of a rectangle's attributes """
        allowed = ['id', 'width', 'height', 'x', 'y']
        if args:
            for att, arg in zip(allowed, args):
                setattr(self, att, arg)
        else:
            for key, value in kwargs.items():
                if key in allowed:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Return dictionary representation of a
        rectangle for json encoding """
        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
