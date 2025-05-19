#!/usr/bin/python3
"""
This module defines a Square class that represents a square geometry.

The Square class contains a private instance attribute to store the size 
of the square. It does not perform any validation on the size value.
"""

class Square:
    """
    Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (no type/value validation).
        
        The size attribute is private, which means it is intended to be 
        accessed only within the class.
        """
        if not isinstance(size, int):
            raise TypeError("must be an integer")
        if size < 0:
            raise ValueError("must be >= 0")
        self.__size = size
