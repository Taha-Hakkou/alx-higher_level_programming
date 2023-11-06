#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """deletes an item at a specific index in a list"""
    if idx >= 0 and idx < len(my_list):
        for i in range(idx, len(my_list)-idx):
            my_list[i] = my_list[i + 1]
        del my_list[len(my_list) - 1]
    return (my_list)
