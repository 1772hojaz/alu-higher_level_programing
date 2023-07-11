#!/usr/bin/python3
def add(a, b):
    value1 = a
    value2 = b
    sum = value1 + value2
    print("{} + {} = {}".format(value1, value2, sum))
    return(sum)

def main():
    add(1,2)

if __name__ == "__main__":
    main()
