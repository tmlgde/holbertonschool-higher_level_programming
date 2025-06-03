#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns
    the number of characters written.

    Args:
        filename (str): Name of the file to write to.
        text (str): Text content to write into the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w") as file:
        return file.write(text)

