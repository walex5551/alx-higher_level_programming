#!/usr/bin/python3
""" Python script that takes 2 arguments: repository name and owner name,
    lists last 10 commits from the repo
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(sys.argv[2], sys.argv[1]))
    for commit in req.json()[:10]:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
