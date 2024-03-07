#!/usr/bin/python3
""" A module to add all arguments to a python list
"""


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import sys
ls = [sys.argv[i] for i in range(1, (len(sys.argv)))]
fildes = open('add_item.json', 'a', encoding="utf-8")
form = load_from_json_file('add_item.json')
form.extend(ls)
save_to_json_file(form, 'add_item.json')
fildes.close()
