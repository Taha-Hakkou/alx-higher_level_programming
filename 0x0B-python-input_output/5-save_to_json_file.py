#!/usr/bin/python3
"""
5-save_to_json_file.py
"""


def save_to_json_file(my_obj, filename):
    """writes an object to a textfile, using a JSON representation"""
    import json
    with open(filename, 'w+', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
