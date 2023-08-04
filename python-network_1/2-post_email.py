#!/usr/bin/python3
# python script that takes your GitHub credentials (username and password),
# and uses the 'GitHub API' to display your 'id'
"""
    use 'GitHub API to display 'id'
"""
import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == '__main__':
    data = urlencode({"email": sys.argv[2]
                      }).encode("ascii")

    request = Request(sys.argv[1], data)
    with urlopen(request) as response:
        print(response.read().decode('utf-8'))
