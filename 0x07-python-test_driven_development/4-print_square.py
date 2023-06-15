#!/usr/bin/python3
"""Defin a function to print square."""


def print_square(size):
    """To print a square based on size given.

    Args:
        size (_int_): _size must be an integer value_

    Raises:
        TypeError: if size in not integer
        ValueError: if size is less than 0
        TypeError:  if size is float and less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
