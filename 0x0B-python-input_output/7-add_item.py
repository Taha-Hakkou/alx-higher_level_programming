#!/usr/bin/python3
"""
7-add_item.py
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys

def main():
    my_list = load_from_json_file('add_item.json') # handle not existing file
    new = []
    for item in sys.argv:
        new.append(item)
    save_to_json_file(my_list + new[1:], 'add_item.json')


if __name__ == '__main__':
    main()
