#!/usr/bin/python3

"""
This module is made up of function that prints a square with the character #

"""
def print_square(size):
    """ Function that prints a square with the character #
    
    Args:
        size: size of the square printed

    Returns:
        No return

    Raises:
        TypeError: If size is not an integer number

    """

    # Check if size is a valid integer or float

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Check if size is non-negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        print("#" * size)
