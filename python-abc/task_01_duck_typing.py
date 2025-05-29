#!/usr/bin/env python3
"""Module defining Shape interface and its concrete implementations
using abstract base classes and duck typing.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius):
        """Initialize a circle with its radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with its width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Print the area and perimeter of any shape-like object."""
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")

