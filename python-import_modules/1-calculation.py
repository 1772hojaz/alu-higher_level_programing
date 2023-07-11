#!/usr/bin/python3


from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    suma = add(a, b)
    print("{} + {} = {}".format(a, b, suma))
    suba = sub(a, b)
    print("{} - {} = {}".format(a, b, suba))
    muil = mul(a, b)
    print("{} * {} = {}".format(a, b, muil))
    dive = div(a, b)
    print("{} / {} = {}".format(a, b, dive))



if __name__ == "__main__":
    main()
