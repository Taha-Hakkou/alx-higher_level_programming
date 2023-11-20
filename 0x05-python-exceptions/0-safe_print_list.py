#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list"""
    """& returns the real number of elements printed"""
    length = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            length += 1
        except IndexError:
            break
    print()
    return (length)
