#!/usr/bin/python3

my_list = [1, 2, 3, 4, 5]

def print_list_integer(my_list=[]):
    for elem in my_list:
        print("{0}".format(elem))

def main():
    print_list_integer(my_list)

if __name__ == "__main__":
    main()
