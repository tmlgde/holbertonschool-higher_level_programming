#!/usr/bin/python3

def roman_to_int(roman_string):
    my_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    total = 0
    prev = 0
    for i in roman_string:
        actuel = my_dict[i]
        if prev < actuel:
            total += actuel - 2 * prev
        else:
            total += actuel
        prev = actuel
    return total
