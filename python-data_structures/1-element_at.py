#!/usr/bin/python3
element_at = __import__('1-element_at').element_at


def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
def main():
    element_at(my_list, idx)


if __name__ == "__main__":
    main()
