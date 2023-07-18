#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])


def main():
    multiple_returns(sentence)
    

if __name__ == "__main__":
    main()
