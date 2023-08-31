#!/bin/bash
# Display the byte size of the HTTP response header for a given URL.
# Sending a request using curl, piping the response to wc to count bytes🤔
# curl -s "$1" | wc -c

url=$1
curl -s "$url" | wc -c
