#!/bin/bash
# Display the byte size of the HTTP response header for a given URL.

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Sending a request using curl and saving the output in a variable
response=$(curl -sI "$url")

# Extracting the content length from the response headers
content_length=$(echo "$response" | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n')

if [ -z "$content_length" ]; then
    # echo "Unable to determine content length."
    exit 1
fi

# echo "Content size: $content_length bytes"
