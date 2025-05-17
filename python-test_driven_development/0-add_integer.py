#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The function ensures that both inputs are either integers
or floats, and will raise a TypeError if not.
"""


def add_integer(a, b):

    """Adds two integers after type validation.
    Returns the sum as an integer.
    Raises TypeError on invalid input."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
