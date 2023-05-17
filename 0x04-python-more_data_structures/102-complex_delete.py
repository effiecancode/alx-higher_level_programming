#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, value in sorted(a_dictionary.items()):
            del a_dictionary[key]
    return a_dictionary
