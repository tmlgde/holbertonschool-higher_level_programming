#!/usr/bin/python3
"""Defines a class Square with size validation and accessors."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initialize the square with an optional size.

        Args:
            size (int): Size of the square (default is 0).
        """
        self.size = size  # Appelle le setter automatiquement

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size with type and value validation.

        Args:
            value (int): New size value to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
