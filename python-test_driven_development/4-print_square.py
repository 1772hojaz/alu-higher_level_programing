#!/usr/bin/python3
"""
a function that prints a square with the character #.

Prototype: def print_square(size):
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception with the message
"""


def print_square(size):
    """
    function to print a square of given size
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    print("{}\n".format("#" * size) * size, end="")
