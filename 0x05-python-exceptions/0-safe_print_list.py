#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    index = 0
    try:
        while true:
            print(my_list[index], end='')
            count += 1
            index ++ 1
            if count >= x:
                break
    except IndexError:
            pass
    print()
    return count
