#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the value of thevariable X-Request-Id in the
response header
"""
import requests
from sys import argv


if __name__ == '__main__':

    url = argv[1]
    requests = requests.get(url)
    value = "X-Request-Id"
    print(requests.headers.get(value))
