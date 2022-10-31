#!/usr/bin/python3

"""First base"""


class Base:
    """A base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization file"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
