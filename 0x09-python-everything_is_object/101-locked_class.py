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
            if type(value) != str:
                raise TypeError("'first_name' attribute must be a string")
            self.__dict__[name] = value
        else:
            m = f"'{self.__class__.__name__}' object has no attribute '{name}'"
            raise AttributeError(m)
