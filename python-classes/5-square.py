#!/usr/bin/python3
"""Defines a Square with property and area."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)