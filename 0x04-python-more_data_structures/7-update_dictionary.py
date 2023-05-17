#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    updated_dict = dict(a_dictionary)
    updated_dict[key] = value
    return updated_dict

def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items())
    for key, value in sorted_dict:
        print(key, value, sep=": ")
