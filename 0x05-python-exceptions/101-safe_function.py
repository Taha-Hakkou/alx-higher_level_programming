#!/usr/bin/python3
def safe_function(fct, *args):
    """executes a function safely"""
    import sys
    try:
        return (fct(*args))
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return (None)
