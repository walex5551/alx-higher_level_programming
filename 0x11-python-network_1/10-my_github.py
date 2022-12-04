#!/usr/bin/python3
""" Script that takes your Github credentials (username and password) and uses
    the Github API to display your id """
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    req = requests.get(url, auth=(argv[1], argv[2]))
    print(req.json().get("id", "None"))
