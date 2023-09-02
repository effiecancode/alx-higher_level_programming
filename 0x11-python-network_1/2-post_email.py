#!/usr/bin/python3
"""A script that:takes in a URL sends a request to the URL
displays the body of the response (decoded in utf-8).
"""
from sys import argv
from urllib import request, error

if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('UTF-8'))

    except error.HTTPError as e:
        print('error code:', e.code)
