#!/usr/bin/python3
"""
This module defines the BaseGeometry class with methods for
area handling and integer validation.
"""


class BaseGeometry:
    """
    BaseGeometry class intended to be extended by other geometry classes.

    Methods:
        area(self): Raises an exception (not implemented).
        integer_validator(self, name, value): Validates integer inputs.
    """

    def area(self):
        """
        Raises an exception to indicate that the method is not yet implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the value (used in exception messages).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
