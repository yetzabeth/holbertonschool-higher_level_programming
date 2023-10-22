#!/usr/bin/python3
"""
Task 4 module: From JSON string to Object
"""
import json


def from_json_string(my_str):
    """Return: an object (Python data structure) represented
    by a JSON string"""
    if my_str is None:
        return
    else:
        return json.loads(my_str)
