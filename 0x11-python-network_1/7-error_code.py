#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL & displays the body of the response
"""
import requests
from sys import argv


if __name__ == '__main__':

    url = argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
