#!/usr/bin/python3


from calculator_1.py import add, sub, mul, div


def main():
    a = 10
    b = 5
    sum = add(a, b)
    print("{} + {} = {}".format(a, b, sum))
    sub = sub(a, b)
    print("{} - {} = {}".format(a, b, sub))
    muil = mul(a, b)
    print("{} * {} = {}".format(a, b, muil))
    dive = div(a, b)
    print("{} / {} = {}".format(a, b, dive))



if __name__ == "__main__":
    main()
