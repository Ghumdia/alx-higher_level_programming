#!/usr/bin/python3
from models.base import Base

"""Defines a rectangle class"""


class Rectangle(Base):
    """Rectangle inherits base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, val):
        self.__width = val

    @height.setter
    def height(self, val):
        self.__height = val

    @x.setter
    def x(self, val):
        self.__x = val

    @y.setter
    def y(self, val):
        self.__y = val
