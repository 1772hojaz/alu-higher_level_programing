#!/usr/bin/python3
'''this funtion adds 2 integers'''

def add_integer(a, b=98):
    '''a funtion that add two integers 
    it has 2 arguments
    '''
    if type(a) == float or type(b)==float:
        a = int(a)
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a+b
