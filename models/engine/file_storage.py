#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
    Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        base_mod = BaseModel()
        u_ser = User()
        st_ate = State()
        pl_ace = Place()
        ci_ty = City()
        amen_ity = Amenity()
        re_view = Review()
        models.storage.new(base_mod)
        models.storage.new(u_ser)
        models.storage.new(st_ate)
        models.storage.new(pl_ace)
        models.storage.new(ci_ty)
        models.storage.new(amen_ity)
        models.storage.new(re_view)
        self.assertIn("BaseModel." + base_mod.id, models.storage.all().keys())
        self.assertIn(base_mod, models.storage.all().values())
        self.assertIn("User." + u_ser.id, models.storage.all().keys())
        self.assertIn(u_ser, models.storage.all().values())
        self.assertIn("State." + st_ate.id, models.storage.all().keys())
        self.assertIn(st_ate, models.storage.all().values())
        self.assertIn("Place." + pl_ace.id, models.storage.all().keys())
        self.assertIn(pl_ace, models.storage.all().values())
        self.assertIn("City." + ci_ty.id, models.storage.all().keys())
        self.assertIn(ci_ty, models.storage.all().values())
        self.assertIn("Amenity." + amen_ity.id, models.storage.all().keys())
        self.assertIn(amen_ity, models.storage.all().values())
        self.assertIn("Review." + re_view.id, models.storage.all().keys())
        self.assertIn(re_view, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        base_mod = BaseModel()
        u_ser = User()
        st_ate = State()
        pl_ace = Place()
        ci_ty = City()
        amen_ity = Amenity()
        re_view = Review()
        models.storage.new(base_mod)
        models.storage.new(u_ser)
        models.storage.new(st_ate)
        models.storage.new(pl_ace)
        models.storage.new(ci_ty)
        models.storage.new(amen_ity)
        models.storage.new(re_view)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_mod.id, save_text)
            self.assertIn("User." + u_ser.id, save_text)
            self.assertIn("State." + st_ate.id, save_text)
            self.assertIn("Place." + pl_ace.id, save_text)
            self.assertIn("City." + ci_ty.id, save_text)
            self.assertIn("Amenity." + amen_ity.id, save_text)
            self.assertIn("Review." + re_view.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        base_mod = BaseModel()
        u_ser = User()
        st_ate = State()
        pl_ace = Place()
        ci_ty = City()
        amen_ity = Amenity()
        re_view = Review()
        models.storage.new(base_mod)
        models.storage.new(u_ser)
        models.storage.new(st_ate)
        models.storage.new(pl_ace)
        models.storage.new(ci_ty)
        models.storage.new(amen_ity)
        models.storage.new(re_view)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_mod.id, objs)
        self.assertIn("User." + u_ser.id, objs)
        self.assertIn("State." + st_ate.id, objs)
        self.assertIn("Place." + pl_ace.id, objs)
        self.assertIn("City." + ci_ty.id, objs)
        self.assertIn("Amenity." + amen_ity.id, objs)
        self.assertIn("Review." + re_view.id, objs)

    def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, models.storage.reload())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
