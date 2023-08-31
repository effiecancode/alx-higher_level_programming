#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
# url=$1
curl -s "$1" | wc -c
