#!/usr/bin/python3
"""6. Create object from a JSON file"""


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object represented by the JSON content.
    """
    import json
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
