#!/usr/bin/python3
"""inherites a list"""


class MyList(list):
    """Implement sorted printing for built-in list class"""
    def print_sorted(self):
        """Returns a sorted list"""
        return(sorted(self))
