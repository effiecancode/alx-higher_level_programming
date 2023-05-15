#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for letters in my_string:
        if letters != 'c' and letters != 'C':
            new_string.append(letters)
    return ''.join(new_string)
