#!/usr/bin/python3
"""Write a function that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file"""
    if my_obj is None:
        return
    else:
        with open(filename, 'w', encoding='utf-8') as file:
            to_write = json.dumps(my_obj)
            file.write(to_write)
