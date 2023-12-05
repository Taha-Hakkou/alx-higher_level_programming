#!/usr/bin/python3
"""
6-load_from_json_file.py
"""


def load_from_json_file(filename):
    """creates an object from a JSON file
    Returns: created object"""
    import json
    with open(filename, 'r', encoding='utf-8') as file:
        obj = json.loads(file.read())
    return (obj)
