#!/usr/bin/python3
"""
Write a class Student that defines a student
"""


class Student():
    """Class Student with attributes"""

    def __init__(self, first_name, last_name, age):
        """To create a new instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if type(attrs) == list:
            new_dict = {}
            for item in attrs:
                for key, value in self.__dict__.items():
                    if key == item:
                        new_dict[item] = value
            return new_dict

        return self.__dict__

    def reload_from_json(self, json):
        return self.__dict__.update(json)
