#!/usr/bin/python3
"""Addition of two integers or floats

This module provides function add_integer(a, b=98) returns the sum of a and b
The function ensures both arguments integers or floats, and raises TypeError
"""


def add_integer(a, b=98):
    """Returns the sum of a and b, casting floats to integers.

    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add, default is 98.

    Returns:
        int: The sum of a and b as integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
