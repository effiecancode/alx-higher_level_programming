#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    index = 0
    new_str = ""
    for element in str:
        if index == n:
            index += 1
            continue
        new_str += str[index]
        index +=1
    return new_str
