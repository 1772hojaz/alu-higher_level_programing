#!/usr/bin/python3
"""Define a square"""


class Square:
    """Creates a square.
    Private instance attributes"""

    def _init_(self, size=0):
        """Initialisation."""
        self.__size = size

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns square area."""
        return self.__size ** 2
