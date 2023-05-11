#!/usr/bin/python
from sys import argv
def argoutput():
    num_args = len(argv)
    if num_args < 2:
        print("{} argument.".format(num_args - 1))
    else:
        if num_args == 2:
            print("{} argument:".format(num_args - 1))
        else:
            print("{} arguments:".format(num_args -1))   
        for n, arg in enumerate (argv[1:], start=1):
            print("{}: {}".format(n, arg))


if __name__ == "__main__":
    argoutput()
