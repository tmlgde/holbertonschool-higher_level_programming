#!/usr/bin/env python3
"""Module defining an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal (to be implemented)."""
        pass


class Dog(Animal):
    """Concrete subclass of Animal representing a dog."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Concrete subclass of Animal representing a cat."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"

