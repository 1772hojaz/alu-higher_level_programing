#!/usr/bin/python3
a = 1
b = 2
from add_0 import add
def main():
    sum = add (a, b)
    print("{} + {} = {}".format(a, b, sum))

if __name__ == "__main__":
    main()
