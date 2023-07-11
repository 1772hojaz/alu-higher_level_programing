#!/usr/bin/python3


import sys


def main(*argv):
    lstring = len(sys.argv) - 1

    if lstring > 1:
        print("{:d} arguments:".format(lstring))
        for i in range(1, len(sys.argv)):
            print("{:d}: {}".format(i, sys.argv[i]))
    elif lstring == 0:
        print("{:d} arguments.".format(lstring))
    else:
        print("{:d} argument:".format(lstring))
        print("{:d}: {}".format(1, sys.argv[1]))


if __name__ == "__main__":
    main()
