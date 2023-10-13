#!/usr/bin/python3
''' Write the first class Base '''
import json
import os


class Base:
    ''' class base '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' constuctor  '''
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' to json  '''
        if list_dictionaries is None:
            return "[]"
        temp = json.dumps(list_dictionaries)
        return temp

    @classmethod
    def save_to_file(cls, list_objs):
        ''' save json in a file  '''
        file = cls.__name__ + ".json"
        temp = []
        if list_objs:
            for i in list_objs:
                temp.append(i.to_dictionary())
        with open(file, "w") as f:
            f.write(Base.to_json_string(temp))

    @staticmethod
    def from_json_string(json_string):
        ''' to string '''

        if json_string is None or json_string == "[]":
            return []
        temp = json.loads(json_string)
        return temp

    @classmethod
    def create(cls, **dictionary):
        ''' create  '''

        if cls.__name__ == 'Rectangle':
            temp = cls(1, 1)
        elif cls.__name__ == 'Square':
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""

        file = cls.__name__ + ".json"
        list_ = []
        list_dicts = []
        if os.path.exists(file):
            with open(file, 'r') as f:
                x = f.read()
                list_dicts = cls.from_json_string(x)
                for i in list_dicts:
                    list_.append(cls.create(**i))
        return list_
