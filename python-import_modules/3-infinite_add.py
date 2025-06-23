#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    number_args = len(args)

    resultat = 0

    for arg in args:
        resultat += int(arg)

    print(resultat)
