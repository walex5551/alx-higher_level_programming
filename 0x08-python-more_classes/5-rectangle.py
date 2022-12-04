#!/usr/bin/python3


class Rectangle:
    """ A class that defines a rectangle

    Attributes:
        width(obj: 'int'): width of a rectangle
        height(obj: 'int'): height of a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Initializes rectangle class
        Args:
            width(obj: 'int') for width attribute
            height(obj: 'int') for height attribute
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Defines width of rectangle object """
        return self.__width

    @width.setter
    def width(self, value):
        """ Defined width the change to value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Defines height of rectangle object """
        return self.__height

    @height.setter
    def height(self, value):
        """ Defined height the change to value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter of rectangle """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Prints rectangle of symbols('#' default) when object is called """
        rect_array = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect_array.append('#')
            rect_array.append('\n')
        del rect_array[-1]
        return ''.join(rect_array)

    def __repr__(self):
        """ Returns string representation to recreate a new instance """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ Delete instance of rectangle """
        print("Bye rectangle...")
