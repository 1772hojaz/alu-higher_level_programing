#!/usr/bin/python3
"""area calculation"""
class Square:
    """we square the side of a square to get its area"""
    def __init__(self, size=0):
        self.__size = size
    def area(self):
        return self.__size**2

