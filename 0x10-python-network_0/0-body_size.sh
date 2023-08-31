#!/bin/bash
# Display the byte size of the HTTP response header for a given URL.
# curl -s "$1" | wc -c

if [ $# -ne 1 ]; then
    exit 1
fi

url=$1

# Sending a request using curl, piping the response to wc to count bytes
content_size=$(curl -s "$url" | wc -c)

