#!/usr/bin/python3

"""MyList class"""


class MyList(list):
    """child class of list"""
    def __init__(self):
        """Initialize"""
        super().__init__()

    def print_sorted(self):
        """Prints sorted list in ascending order"""
        print(sorted(self))