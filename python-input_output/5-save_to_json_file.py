#!/usr/bin/python3
"""5. Save Object to a file"""


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
