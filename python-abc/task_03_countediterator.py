#!/usr/bin/env python3
"""Module defining CountedIterator:
an iterator that counts how many items have been returned.
"""


class CountedIterator:
    """Custom iterator that wraps an iterable and counts iterations."""

    def __init__(self, iterable):
        """Initialize the iterator and the counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the counter."""
        self.count += 1
        item = next(self.iterator)
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count

