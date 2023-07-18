#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list


def main():
    search_replace(my_list, seach, replace)


if __name__ == "__main__":
    main()
