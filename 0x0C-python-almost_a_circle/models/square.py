#!/usr/bin/python3
"""
square - 1 class

"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square made out of rectangle attrs and size

        Attributes:
            size(obj : 'int'): side length
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ initalization

            Args:
                size: side length
                x(obj : 'int'): offset for x coordinate
                y(obj : 'int'): offset for y coordinate
                id(obj : 'int'): id of created square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Print elements of square """

        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__width)
        return s

    @property
    def size(self):
        """ Find size attribute """

        return self.__width

    @size.setter
    def size(self, value):
        """ Set size attribute

            Since we're making a square,
            width and height are the same
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """ Update square with new attributes

            Args:
                self('class'): entire square class
                args(obj : 'list'): list of attribute wanting to change
                kwargs(obj : 'dict'): key value pair to change
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                setattr(self, 'id', args[0])
            if len(args) > 1:
                setattr(self, 'size', args[1])
            if len(args) > 2:
                setattr(self, 'x', args[2])
            if len(args) > 3:
                setattr(self, 'y', args[3])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Make dictionary of square for json encoding """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
