#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = 0
    for key in a_dictionary:
        if a_dictionary[key] > best_score:
             best_score = a_dictionary[key]
    return best_score   
