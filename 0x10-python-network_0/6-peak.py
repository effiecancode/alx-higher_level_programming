#!/bin/bash/python3
"""function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """fuction that finds the peak of a list"""
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1

        else:
            right = mid

    return list_of_integers
