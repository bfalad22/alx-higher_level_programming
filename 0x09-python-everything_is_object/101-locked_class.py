#!/usr/bin/python3

"""

This is a module that contains a class that avoids dynamically created attributes

"""

    class LockedClass:
        _slots_ = ['first_name']

        def _init_(self):
            """Init method"""
            pass

