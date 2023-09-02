#!/usr/bin/python3
"""A script that:takes in a URL sends a request to the URL
displays the body of the response (decoded in utf-8).
"""
from sys import argv
from urllib import request, parse

if __name__ == "__main__":

    url = argv[1]
    emailvar = {'email': argv[2]}

    data = parse.urlencode(emailvar).encode('utf-8')
    requests = request.Request(argv[1], data)
    with request.urlopen(requests) as response:
        print(response.read().decode('UTF-8'))
