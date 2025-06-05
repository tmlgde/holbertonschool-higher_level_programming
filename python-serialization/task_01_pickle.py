#!/usr/bin/env python3
"""Module for pickling and unpickling a custom Python object."""

import pickle


class CustomObject:
    """
    A custom object with name, age, and is_student attributes.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
    """

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        Args:
            filename (str): The name of the file to write the object to.
        """
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): The name of the file to read the object from.

        Returns:
            CustomObject or None: The deserialized object,
            or None if an error occurs.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
