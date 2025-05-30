#!/usr/bin/python3
"""
Simple OOP example using abstract base classes and duck typing.
Defines Shape, Circle, Rectangle, and a utility function to print shape info.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape with a radius."""

    def __init__(self, radius):
        """Initialize circle with given radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return self.radius * self.radius * math.pi

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape with height and width."""

    def __init__(self, height, width):
        """Initialize rectangle with height and width."""
        self.height = height
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.height + self.width)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    Args:
        shape (Shape): An instance of a shape.
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))

