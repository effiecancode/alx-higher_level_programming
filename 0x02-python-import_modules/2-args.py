#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
argn = len(argv)
if argn < 2:
    print("{} arguments.".format(argn - 1))
else:
    if argn == 2:
        print("{} argument:".format(argn - 1))
    else:
        print("{} arguments:".format(argn - 1))
    for i in range(1, argn):
        print("{}: {}".format(n, argv[i]))
