#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    total_w = 0
    total_s = 0
    if len(my_list) <= 0:
        return 0

    for item in my_list:
        score, weight = item
        total_w += weight
        total_s += score * weight

    result = total_s / total_w
    return result
