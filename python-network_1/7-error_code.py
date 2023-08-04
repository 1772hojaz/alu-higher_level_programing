#!/usr/bin/python3
# python script that takes in a URL and an email address,

"""
    send a POST request to the passed URL with the email as a parameter,
    & displaysthe body of the response
"""
if __name__ == '__main__':
    import requests
    import sys
    request = requests.get(sys.argv[1])
    if request.status_code < 400:
        print(request.text)
    elif request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
