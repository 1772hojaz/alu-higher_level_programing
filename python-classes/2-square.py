#!/usr/bin/python3

"""this is an empty class
its about  asquare"""


class Square:
    """This is the class"""
    def __init__(self, size=0):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size_new):
        if type(size_new) is not int:
            raise TypeError("size must be an integer")

        if size_new < 0:
            raise ValueError("size must be >= 0")
