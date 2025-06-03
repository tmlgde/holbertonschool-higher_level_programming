#!/usr/bin/python3
"""4. From JSON string to Object"""


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python data structure.
    """
    import json
    return json.loads(my_str)

