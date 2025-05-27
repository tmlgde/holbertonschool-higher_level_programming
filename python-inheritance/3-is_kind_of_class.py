#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class or a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or a subclass of it.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance of a_class or inherits from it, False otherwise.
    """
    return isinstance(obj, a_class)
