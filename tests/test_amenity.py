#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amen_ity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amen_ity.__dict__)

    def test_two_amenities_unique_ids(self):
        amen_ity1 = Amenity()
        amen_ity2 = Amenity()
        self.assertNotEqual(amen_ity1.id, amen_ity2.id)

    def test_two_amenities_different_created_at(self):
        amen_ity1 = Amenity()
        sleep(0.05)
        amen_ity2 = Amenity()
        self.assertLess(amen_ity1.created_at, amen_ity2.created_at)

    def test_two_amenities_different_updated_at(self):
        amen_ity1 = Amenity()
        sleep(0.05)
        amen_ity2 = Amenity()
        self.assertLess(amen_ity1.updated_at, amen_ity2.updated_at)

    def test_str_representation(self):
        date_time = datetime.today()
        dt_repr = repr(date_time)
        amen_ity = Amenity()
        amen_ity.id = "123456"
        amen_ity.created_at = amen_ity.updated_at = date_time
        amstr = amen_ity.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        amen_ity = Amenity(None)
        self.assertNotIn(None, amen_ity.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        date_time = datetime.today()
        dt_iso = date_time.isoformat()
        amen_ity = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amen_ity.id, "345")
        self.assertEqual(amen_ity.created_at, date_time)
        self.assertEqual(amen_ity.updated_at, date_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

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
        amen_ity = Amenity()
        sleep(0.05)
        first_updated_at = amen_ity.updated_at
        amen_ity.save()
        self.assertLess(first_updated_at, amen_ity.updated_at)

    def test_two_saves(self):
        amen_ity = Amenity()
        sleep(0.05)
        first_updated_at = amen_ity.updated_at
        amen_ity.save()
        second_updated_at = amen_ity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amen_ity.save()
        self.assertLess(second_updated_at, amen_ity.updated_at)

    def test_save_with_arg(self):
        amen_ity = Amenity()
        with self.assertRaises(TypeError):
            amen_ity.save(None)

    def test_save_updates_file(self):
        amen_ity = Amenity()
        amen_ity.save()
        amid = "Amenity." + amen_ity.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amen_ity = Amenity()
        self.assertIn("id", amen_ity.to_dict())
        self.assertIn("created_at", amen_ity.to_dict())
        self.assertIn("updated_at", amen_ity.to_dict())
        self.assertIn("__class__", amen_ity.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amen_ity = Amenity()
        amen_ity.middle_name = "ALX"
        amen_ity.my_number = 98
        self.assertEqual("ALX", amen_ity.middle_name)
        self.assertIn("my_number", amen_ity.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amen_ity = Amenity()
        am_dict = amen_ity.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        date_time = datetime.today()
        amen_ity = Amenity()
        amen_ity.id = "123456"
        amen_ity.created_at = amen_ity.updated_at = date_time
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(amen_ity.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        amen_ity = Amenity()
        self.assertNotEqual(amen_ity.to_dict(), amen_ity.__dict__)

    def test_to_dict_with_arg(self):
        amen_ity = Amenity()
        with self.assertRaises(TypeError):
            amen_ity.to_dict(None)


if __name__ == "__main__":
    unittest.main()
