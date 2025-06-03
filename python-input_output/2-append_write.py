#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8)
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to write at the end of the file.

    Returns:
        int: Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

