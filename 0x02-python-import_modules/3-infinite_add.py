#!/usr/bin/python3
import sys


def add_args():
    n = len(sys.argv)
    total = 0
    for i in range(1, n):
        total += int(sys.argv[i])
    print(total)


if __name__ == "__main__":
    add_args()
