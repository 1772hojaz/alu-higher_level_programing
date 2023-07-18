#!/usr/bin/python3
def uniq_add(my_list):
    unique_set = set(my_list)
    total_sum = sum(unique_set)
    return total_sum


def main():
    uniq_add(my_list)


if __name__ == "__main__":
    main()
