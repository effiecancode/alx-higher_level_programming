#!/usr/bin/python3
"""A script that: takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable found in the header ofthe response.
"""
from sys import argv
from urllib import request

if __name__ == "__main__":
    url = argv[1]

    req = request.Request(url)
    with request.urlopen(req) as response:
        header = "X-Request-Id"
        print(dict(response.headers).get(header))
