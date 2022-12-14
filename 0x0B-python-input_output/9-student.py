#!/usr/bin/python3
"""Defines a student class"""


class Student:
    """module for student"""
    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrives dict"""
        return self.__dict__
