#!/bin/bash
# sends a json post request to a url passed as the first argument, and displays the body of the response
curl -s -X POST $1 -H "Content-Type: application/json" -d @$2
