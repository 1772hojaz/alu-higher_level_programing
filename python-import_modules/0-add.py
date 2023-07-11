#!/usr/bin/python3

import add_0 as addition

def main():
    a = 1
    b = 2
    sum = addition.add(a, b)
    print("{} + {} = {}".format(a, b, sum))

if __name__ == "__main__":
    main()
