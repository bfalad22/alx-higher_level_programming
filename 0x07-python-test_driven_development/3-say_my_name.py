#!/usr/bin/python3
"""Defin say my name funcrion"""


def say_my_name(first_name, last_name=""):
    """A function that display first-name and last_nname.

    Raise:
    TypeError: if first_name and last_name is not a str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

