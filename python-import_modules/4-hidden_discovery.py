#!/usr/bin/python3


import imp

def print_hidden_names(module_path):
  module = imp.load_compiled("hidden_4", module_path)
  names = [name for name in dir(module) if not name.startswith("__")]
  names.sort()
  for name in names:
    print(name)

if __name__ == "__main__":
  print_hidden_names("hidden_4.pyc")
