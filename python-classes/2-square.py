#!/usr/bin/python3

"""this is an empty class
its about  asquare"""


class Square:
    """This is the class"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")

        elif size_new < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
