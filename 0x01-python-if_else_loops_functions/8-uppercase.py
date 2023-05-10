#!/usr/bin/python3
def uppercase(s):

    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print("{}".format(chr(ord(c) - ord('a') + ord('A'))), end="")
        else:
            print("{}".format(c), end="")
    print()
