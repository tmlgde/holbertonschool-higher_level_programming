#!/usr/bin/env python3
"""Module to convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert CSV data from a file to JSON format and save it to 'data.json'.

    Args:
        filename (str): The name of the CSV file to read.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        with open(filename, "r") as file:
            rows = list(csv.DictReader(file))

        with open("data.json", "w") as file:
            json.dump(rows, file)

        return True
    except Exception:
        return False

