#!/usr/bin/python3
""" Script that takes in a string and sends a search request to the Star Wars
    API
"""
import requests
import sys


if __name__ == "__main__":
    a = sys.argv[1]
    req = requests.get('https://swapi.co/api/people/?search={}'.format(a))
    req_json = req.json()
    li = req_json.get('results')
    print('Number of results: {}'.format(req_json.get('count')))
    while req_json.get('next'):
        res = requests.get(req_json.get('next'))
        new_json = res.json()
        li += new_json.get('results')
    for result in li:
        print(result.get('name'))
