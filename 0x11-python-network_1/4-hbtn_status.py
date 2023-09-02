#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == '__main__':

    requests = requests.get('https://alx-intranet.hbtn.io/status')
    text = requests.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
