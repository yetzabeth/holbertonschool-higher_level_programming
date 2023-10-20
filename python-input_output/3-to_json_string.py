#!/usr/bin/python3
"""
Write a function that returns
the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    if my_obj is None:
        return
    else:
        return json.dumps(my_obj)
