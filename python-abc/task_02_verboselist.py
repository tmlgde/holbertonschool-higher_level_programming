#!/usr/bin/env python3
"""Module defining VerboseList, an extension of Python's list
that prints notifications on item changes.
"""


class VerboseList(list):
    """Custom list class that notifies on modifications."""

    def append(self, item):
        """Append an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """Extend the list with an iterable and print a notification."""
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a notification."""
        val = super().pop(index)
        print(f"Popped [{val}] from the list.")
        return val

