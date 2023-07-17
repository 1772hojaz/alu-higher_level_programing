#!/usr/bin/python3


my_list = [1, 2, 3, 4, 5]
def main ():
    for idx, elem in enumerate(my_list):
        print("Element at index {:d} is {}".format(idx, elem))


if __name__ == "__main__":
    main()
