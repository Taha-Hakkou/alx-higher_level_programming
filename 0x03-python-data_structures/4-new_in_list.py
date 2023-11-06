#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific position
       without modifying the original list """
    new = my_list.copy()
    if idx >= 0 and idx < len(new):
        new[idx] = element
    return (new)
