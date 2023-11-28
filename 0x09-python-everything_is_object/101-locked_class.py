#!/usr/bin/python3
"""
101-locked_class.py
"""


class LockedClass:
    """locked class"""

    def __setattr__(self, name, value):
        """prevents dynamic creation of new instance attributes,
        except if the new instance attribute is called first_name"""
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
