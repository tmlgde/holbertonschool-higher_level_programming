#!/usr/bin/python3
"""Defines a Square class with size and position."""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square.

        Args:
            size (int): Size of the square (default 0).
            position (tuple): Position tuple (default (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' at the given position."""
        if self.__size == 0:
            print()
            return

        # Print newlines for vertical position (position[1])
        for _ in range(self.__position[1]):
            print()

        # Print the square with spaces for horizontal position
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
