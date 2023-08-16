#!/usr/bin/python3
"""Write a function that prints a text with
2 new lines after each of these characters: ., ? and :

Prototype: def text_indentation(text):
text must be a string, otherwise
raise a TypeError exception
with the message text must be a string
"""


def text_indentation(text):
    """prints text with 2 newlines after '.' '?' or ':' chars"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    previous = ""
    for char in text:
        # leading whitespace
        if char is " " and char is text[0] and previous is "":
            previous = "\n"
            continue
        # whitespaces after newline
        if char is " " and previous is "\n":
            continue
        # matching character, print char, print newlines
        if char is "." or char is "?" or char is ":":
            print(char)
            print()
            previous = "\n"
        else:
            print(char, end="")
            previous = char
