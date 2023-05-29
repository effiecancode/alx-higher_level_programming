#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for num in range(x):
        try:
                print(my_list[num], end=' ')
                count += 1
    except Exception as err:
        break

    print('')
    return count
