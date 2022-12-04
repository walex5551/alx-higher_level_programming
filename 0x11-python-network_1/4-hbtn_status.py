#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(req)))
    print("\t- content: {}".format(req))
