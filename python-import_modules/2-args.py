#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    number_args = len(args)

    if number_args == 0:
        print("0 arguments.")

    elif number_args == 1:
        print("{} argument:".format(number_args))
    else:
        print("{} arguments:".format(number_args))

        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
