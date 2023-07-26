#!/usr/bin/python3

"""area calculation"""


class Square:
    """private instance attribute: size"""
    def __init__(self, size=0):
        self.__size = size


    @property
    """this is to get the private value of size a private attribute. we use getter method"""
    def size(self):
        return self.__size = size


    @size.setter
    """this is to make sure that the value that we got with the getter can be used and or modified """
    def size(self, value):
        """to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        """if size is less than 0, raise a ValueError exception with the message size must be >= 0"""
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value


"""Public instance method: def area(self): that returns the current square area"""
    def area(self):
        return self.__size**2
