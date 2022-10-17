#!/usr/bin/python3


"""Represents a reactangle"""


class Rectangle:
    """Define Rectangle"""
    def __init__(self, width=0, height=0):
        """initialize a new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of rectangle"""
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @width.setter
    def width(self, value):
        """sets a new width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets a new height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
