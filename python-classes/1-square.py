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

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (no type/value validation).
        
        The size attribute is private, which means it is intended to be 
        accessed only within the class.
        """
        self.__size = size
