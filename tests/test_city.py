#!/usr/bin/python3
"""Defines unittests for models/city.py.
Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        ci_ty = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(ci_ty))
        self.assertNotIn("state_id", ci_ty.__dict__)

    def test_name_is_public_class_attribute(self):
        ci_ty = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(ci_ty))
        self.assertNotIn("name", ci_ty.__dict__)

    def test_two_cities_unique_ids(self):
        ci_ty1 = City()
        ci_ty2 = City()
        self.assertNotEqual(ci_ty1.id, ci_ty2.id)

    def test_two_cities_different_created_at(self):
        ci_ty1 = City()
        sleep(0.05)
        ci_ty2 = City()
        self.assertLess(ci_ty1.created_at, ci_ty2.created_at)

    def test_two_cities_different_updated_at(self):
        ci_ty1 = City()
        sleep(0.05)
        ci_ty2 = City()
        self.assertLess(ci_ty1.updated_at, ci_ty2.updated_at)

    def test_str_representation(self):
        date_time = datetime.today()
        dt_repr = repr(date_time)
        ci_ty = City()
        ci_ty.id = "123456"
        ci_ty.created_at = ci_ty.updated_at = date_time
        cystr = ci_ty.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        ci_ty = City(None)
        self.assertNotIn(None, ci_ty.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_time = datetime.today()
        dt_iso = date_time.isoformat()
        ci_ty = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(ci_ty.id, "345")
        self.assertEqual(ci_ty.created_at, date_time)
        self.assertEqual(ci_ty.updated_at, date_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

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
        ci_ty = City()
        sleep(0.05)
        first_updated_at = ci_ty.updated_at
        ci_ty.save()
        self.assertLess(first_updated_at, ci_ty.updated_at)

    def test_two_saves(self):
        ci_ty = City()
        sleep(0.05)
        first_updated_at = ci_ty.updated_at
        ci_ty.save()
        second_updated_at = ci_ty.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        ci_ty.save()
        self.assertLess(second_updated_at, ci_ty.updated_at)

    def test_save_with_arg(self):
        ci_ty = City()
        with self.assertRaises(TypeError):
            ci_ty.save(None)

    def test_save_updates_file(self):
        ci_ty = City()
        ci_ty.save()
        city_id = "City." + ci_ty.id
        with open("file.json", "r") as f:
            self.assertIn(city_id, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        ci_ty = City()
        self.assertIn("id", ci_ty.to_dict())
        self.assertIn("created_at", ci_ty.to_dict())
        self.assertIn("updated_at", ci_ty.to_dict())
        self.assertIn("__class__", ci_ty.to_dict())

    def test_to_dict_contains_added_attributes(self):
        ci_ty = City()
        ci_ty.middle_name = "ALX"
        ci_ty.my_number = 98
        self.assertEqual("ALX", ci_ty.middle_name)
        self.assertIn("my_number", ci_ty.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        ci_ty = City()
        cy_dict = ci_ty.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_output(self):
        date_time = datetime.today()
        ci_ty = City()
        ci_ty.id = "123456"
        ci_ty.created_at = ci_ty.updated_at = date_time
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(ci_ty.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        ci_ty = City()
        self.assertNotEqual(ci_ty.to_dict(), ci_ty.__dict__)

    def test_to_dict_with_arg(self):
        ci_ty = City()
        with self.assertRaises(TypeError):
            ci_ty.to_dict(None)


if __name__ == "__main__":
    unittest.main()
