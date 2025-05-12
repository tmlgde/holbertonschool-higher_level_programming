#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for number in ligne:
            print("{:d} ".format(number), end="")
        print()

