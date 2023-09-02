#!/usr/bin/env bash
"""Write a Python script that fetches
https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')

    print("Body response: ")
    print("\t- type: {}".format(type(content)))
    print("\t- content: ", content)

    # except urllib.error.URLerror as e:
    #     print("Error: ", e)
