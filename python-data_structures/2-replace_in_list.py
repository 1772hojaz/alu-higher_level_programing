#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or >= len(my_list):
        return my_list
    my_list[idx] = element


def main():
    replace_in_list(my_list, idx, element)


if __name__ == "__main__":
    main()
