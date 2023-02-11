#!/usr/bin/python3
"""command-line args"""


from sys import argv
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    args_list = load(filename)
except FileNotFoundError:
    args_list = []

for args in argv[1:]:
    args_list.append(args)

save(args_list, filename)
