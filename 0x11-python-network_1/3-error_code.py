#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL &
displays the body of the response (decoded in utf-8)
"""
from urllib import error, request
from sys import argv


if __name__ == "__main__":

    requests = request.Request(argv[1])
    try:
        with request.urlopen(requests) as response:
            print(response.read().decode('utf-8'))

    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
