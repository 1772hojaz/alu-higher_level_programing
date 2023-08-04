#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL"""


if __name__ == '__main__':
    import requests
    import sys
    request = requests.get(sys.argv[1])
    if request.status_code < 400:
        print(request.text)
    elif request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
