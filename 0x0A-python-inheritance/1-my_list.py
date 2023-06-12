#!/usr/bin/python3

"""define MyList class"""


class MyList(list):
    """child class of list"""

    def print_sorted(self):
        """Prints sorted list in ascending order"""
        print(sorted(self))