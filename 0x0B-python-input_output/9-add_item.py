#!/usr/bin/python3
import json
import sys
"""
9-add_item : 0 functions

"""


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    l = load_from_json_file('add_item.json')
except FileNotFoundError:
    l = []
for arg in sys.argv:
    if arg is sys.argv[0]:
        continue
    l.append(arg)
save_to_json_file(l, 'add_item.json')
