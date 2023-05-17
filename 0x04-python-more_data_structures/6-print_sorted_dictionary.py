#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.keys())
    for key in sorted_dict:
        print(key, ": ", a_dictionary[key])
