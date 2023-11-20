#!/usr/bin/python3
def safe_print_division(a, b):
    """divides 2 integers and prints the result"""
    try:
        result = a / b
        print("Inside result: {}".format(result))
    except ZeroDivisionError:
        result = None
        print("Inside result: {}".format(result))
    finally:
        return (result)
