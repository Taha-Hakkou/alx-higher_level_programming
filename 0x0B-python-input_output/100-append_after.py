#!/usr/bin/python3
"""
100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing a specific string"""
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        if search_string in line:
            lines.insert(lines.index(line) + 1, new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)
