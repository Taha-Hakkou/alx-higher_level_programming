#!/usr/bin/python3
"""
7-add_item.py
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    myList = []
    try:
        myList = load_from_json_file('add_item.json')
    except Exception:
        pass
    for item in sys.argv[1:]:
        myList.append(item)
    save_to_json_file(myList, 'add_item.json')


if __name__ == '__main__':
    main()
