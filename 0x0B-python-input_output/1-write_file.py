#!/usr/bin/python3
"""
1-write_file.py
"""


def write_file(filename="", text=""):
    """writes a string to a text file (utf-8)
    Returns: number of characters writen"""
    with open(filename, 'w+', encoding='utf-8') as file:
        file.write(text)
    return (len(text))

