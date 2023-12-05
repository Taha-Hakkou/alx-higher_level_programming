#!/usr/bin/python3
"""
4-from_json_string.py
"""


def from_json_string(my_str):
    """Returns: object (python data structure) represented by a JSON string"""
    import json
    return (json.loads(my_str))
