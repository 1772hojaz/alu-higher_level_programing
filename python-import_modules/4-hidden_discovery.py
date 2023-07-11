#!/usr/bin/python3


import marshal


def print_module_names():
    with open("hidden_4.pyc", "rb") as file:
        code_object = marshal.load(file)
    names = code_object.co_names
    names = sorted(name for name in names if not name.startswith("__"))
    for name in names:
        print(name)


if __name__ == "__main__":
    print_module_names()
