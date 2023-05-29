#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    iterator = iter(my_list)

    while count < x:
        try:
            index = next(iterator)
            print("{:d}".format(my_list[index]), end="")
            count += 1
        except (ValueError, TypeError, StopIteration):
            continue

    print()
    return count
