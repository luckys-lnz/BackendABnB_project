#!/usr/bin/python3
""" A storage module"""
import json
from os.path import isfile


class FileStorage:
    """
        FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __object to the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        dict_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(dict_obj, f)

    def reload(self):
        """
            deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists
        """
        if isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                dict_obj = json.load(f)
                for key, data_obj in dict_obj.items():
                    class_name, obj_id = key.split('.')
                    data_obj['__class__'] = class_name
                    instance_obj = eval(class_name)(**data_obj)
                    self.new(instance_obj)

