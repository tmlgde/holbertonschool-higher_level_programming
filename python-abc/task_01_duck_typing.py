#!/usr/bin/env python3
"""Module defining shapes with abstract base class and duck typing."""

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
    """Circle shape with a given radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return abs(2 * pi * self.radius)


class Rectangle(Shape):
    """Rectangle shape with given width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of the shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

