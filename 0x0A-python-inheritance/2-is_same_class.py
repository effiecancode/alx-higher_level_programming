#!/usr/bin/python3
"""Function is_same_clas"""


def is_same_class(obj, a_class):
    """
    return true if obj is the exact class a_class, otherwise false
    """
    return (type(obj) == a_class)