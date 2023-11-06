#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """deletes an item at a specific index in a list"""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
