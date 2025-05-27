#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    Validates width and height as positive integers.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance after validating width and height.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Format: [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
