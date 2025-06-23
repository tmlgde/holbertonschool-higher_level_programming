#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """
    BaseGeometry class intended to be extended by other geometry classes.

    Methods:
        area(self): Raises an Exception indicating it is not implemented.
    """

    def area(self):
        """
        Raises an exception to indicate that the method is not yet implemented.

        This method should be overridden by subclasses.
        """
        raise Exception("area() is not implemented")
