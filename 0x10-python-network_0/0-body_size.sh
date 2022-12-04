#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl $1 -sI | grep Content-Length | cut -f2 -d' '
