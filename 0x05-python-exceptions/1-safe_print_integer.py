#!/usr/bin/python3
def safe_print_interger(value):
    try:
        print("{:d}".format(value))
        print()
        return True
    except (ValueErroe, TypeError):
        return False
