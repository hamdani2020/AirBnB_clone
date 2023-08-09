#!/usr/bin/python3
"""Defines unittests for models/user.py.
Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        u_ser1 = User()
        u_ser2 = User()
        self.assertNotEqual(u_ser1.id, u_ser2.id)

    def test_two_users_different_created_at(self):
        u_ser1 = User()
        sleep(0.05)
        u_ser2 = User()
        self.assertLess(u_ser1.created_at, u_ser2.created_at)

    def test_two_users_different_updated_at(self):
        u_ser1 = User()
        sleep(0.05)
        u_ser2 = User()
        self.assertLess(u_ser1.updated_at, u_ser2.updated_at)

    def test_str_representation(self):
        date_time = datetime.today()
        dt_repr = repr(date_time)
        u_ser = User()
        u_ser.id = "123456"
        u_ser.created_at = u_ser.updated_at = date_time
        usstr = u_ser.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_args_unused(self):
        u_ser = User(None)
        self.assertNotIn(None, u_ser.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_time = datetime.today()
        dt_iso = date_time.isoformat()
        u_ser = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(u_ser.id, "345")
        self.assertEqual(u_ser.created_at, date_time)
        self.assertEqual(u_ser.updated_at, date_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        u_ser = User()
        sleep(0.05)
        first_updated_at = u_ser.updated_at
        u_ser.save()
        self.assertLess(first_updated_at, u_ser.updated_at)

    def test_two_saves(self):
        u_ser = User()
        sleep(0.05)
        first_updated_at = u_ser.updated_at
        u_ser.save()
        second_updated_at = u_ser.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        u_ser.save()
        self.assertLess(second_updated_at, u_ser.updated_at)

    def test_save_with_arg(self):
        u_ser = User()
        with self.assertRaises(TypeError):
            u_ser.save(None)

    def test_save_updates_file(self):
        u_ser = User()
        u_ser.save()
        usid = "User." + u_ser.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        u_ser = User()
        self.assertIn("id", u_ser.to_dict())
        self.assertIn("created_at", u_ser.to_dict())
        self.assertIn("updated_at", u_ser.to_dict())
        self.assertIn("__class__", u_ser.to_dict())

    def test_to_dict_contains_added_attributes(self):
        u_ser = User()
        u_ser.middle_name = "ALX"
        u_ser.my_number = 98
        self.assertEqual("ALX", u_ser.middle_name)
        self.assertIn("my_number", u_ser.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        u_ser = User()
        us_dict = u_ser.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        date_time = datetime.today()
        u_ser = User()
        u_ser.id = "123456"
        u_ser.created_at = u_ser.updated_at = date_time
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(u_ser.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        u_ser = User()
        self.assertNotEqual(u_ser.to_dict(), u_ser.__dict__)

    def test_to_dict_with_arg(self):
        u_ser = User()
        with self.assertRaises(TypeError):
            u_ser.to_dict(None)


if __name__ == "__main__":
    unittest.main()
