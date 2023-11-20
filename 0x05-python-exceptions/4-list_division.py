#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists"""
    """& Returns a new list with all divisions"""
    new_list = []
    for i in range(list_length):
        try:
            element = my_list_1[i] / my_list_2[i]
        except IndexError:
            element = 0
            print("out of range")
        except (TypeError, ValueError): # not integer or float
            element = 0
            print("wrong type")
        except ZeroDivisionError:
            element = 0
            print("division by 0")
        finally:
            new_list.append(element)
    return (new_list)
