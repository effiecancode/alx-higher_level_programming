#!/usr/bin/python3
import hidden_4


def print_all():
    file = dir(hidden_4)
    length = len(file)
    for i in range(0, length):
        if file[i] [0:2] != "__":
            print(file[i])


if __name__ == "__main__":
    print_all()
