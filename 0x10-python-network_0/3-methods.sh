#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl $1 -sI | grep Allow | cut -f2- -d' '
