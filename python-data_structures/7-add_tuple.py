#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    somme1 = tuple_a[0] + tuple_b[0]
    somme2 = tuple_a[1] + tuple_b[1]

    return (somme1, somme2)
