#!/usr/bin/python3
"""
2-append_write.py
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (utf-8)
    Returns: number of characters added"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return (len(text))
