#!/usr/bin/python3
"""
0-read_file.py
"""


def read_file(filename=""):
    """reads a text file (utf-8) & prints it to stdout"""
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
    print(read_data, end='')
