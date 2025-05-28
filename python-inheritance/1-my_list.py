#!/usr/bin/python3
"""This module defines the MyList class that extends the built-in list
with a method to print its elements sorted."""


class MyList(list):

    """MyList is a custom list that inherits from the built-in list
    and adds a method to print its elements in sorted order."""

    def print_sorted(self):
        """Prints the elements of the list
        in ascending order without modifying the original list."""

        print("{}".format(sorted(self)))
