#!/usr/bin/python3
"""
This module provides a function to list
available attributes and methods of an object.
"""


def lookup(obj):
    """
    Return a list of all attributes and methods
    available for the given object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attribute/method names.
    """
    return dir(obj)
