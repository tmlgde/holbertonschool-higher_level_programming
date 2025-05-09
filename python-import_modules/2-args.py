#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    number_args = len(args)

    if number_args == 0:
        print("0 arguments.")

    elif number_args == 1:
        print("1 argument:")
        print("1: {}".format(args[0]))
    else:
        print("{} arguments:".format(number_args))

        for i in range(number_args):
            print("{}: {}".format(i + 1, args[i]))
