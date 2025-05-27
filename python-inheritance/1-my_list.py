#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
"""


class MyList(list):
    """
    MyList class that inherits from the built-in list.

    Adds a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.

        The original list remains unchanged.
        """
        print(sorted(self))
