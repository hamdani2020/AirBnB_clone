#!/usr/bin/python3
"""File storage module"""
import datetime
import json
import os


class FileStorage:
    """Serialization and deserialization of base class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """It returns objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            data = {a: b.to_dict() for a, b in FileStorage.__objects.items()}
            json.dump(data, f)
    def classes(self):
        """It returns valid class dictionaries"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "Amenity": Amenity,
                   "City": City,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {a: self.classes()[b["__class__"]](**b)
                    for a, b in obj_dict.items()}
            FileStorage.__objects = obj_dict

