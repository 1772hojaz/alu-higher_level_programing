#!/usr/bin/python3
element_at = __import__('1-element_at').element_at


my_list = [1, 2, 3, 4, 5]
def main ():
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]


if __name__ == "__main__":
    main()
