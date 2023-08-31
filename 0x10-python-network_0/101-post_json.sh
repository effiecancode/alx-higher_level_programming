#!/bin/bash
# Sends a JSON POST request to a given URL with a JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
