#!/usr/bin/python3
"""The base class(parent class for the project)"""

class Base:
    """
    Represents the "Parent class" for all other classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
