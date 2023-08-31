#!/bin/bash
# Sends a POST request to a URL
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
