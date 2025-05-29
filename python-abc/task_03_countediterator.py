#!/usr/bin/env python3
"""Module defining CountedIterator, an iterator that counts how many
items have been returned during iteration.
"""


class CountedIterator:
    """Custom iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and set the count to zero."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the count."""
        self.count += 1
        item = next(self.iterator)
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count

