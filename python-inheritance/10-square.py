#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Instantiated with a single size value, validated as a positive integer.
    """

    def __init__(self, size):
        """
        Initialize a Square with size, validated as a positive integer.

        Args:
            size (int): The size of the square (must be > 0).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

