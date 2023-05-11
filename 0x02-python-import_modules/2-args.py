#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
nums = len(argv)
if nums < 2:
    print("{} arguments.".format(nums - 1))
else:
    if nums == 2:
        print("{} argument:".format(nums - 1))
    else:
        print("{} arguments:".format(nums - 1))
    for i in range(1, nums):
        print("{}: {}".format(i, argv[i]))
