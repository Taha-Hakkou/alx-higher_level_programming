#!/usr/bin/python3
"""
7-add_item.py
"""


def main():
    my_list = load_from_json_file('add_item.json')
    for item in sys.argv:
        my_list.append(item)
    save_to_json_file('add_item.json', my_list)

if __name__ == '__main__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    import sys
    main()
