#!/usr/bin/python3
"""Defines unittests for models/place.py.
Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        pl_ace = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl_ace))
        self.assertNotIn("city_id", pl_ace.__dict__)

    def test_user_id_is_public_class_attribute(self):
        pl_ace = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl_ace))
        self.assertNotIn("user_id", pl_ace.__dict__)

    def test_name_is_public_class_attribute(self):
        pl_ace = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl_ace))
        self.assertNotIn("name", pl_ace.__dict__)

    def test_description_is_public_class_attribute(self):
        pl_ace = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl_ace))
        self.assertNotIn("desctiption", pl_ace.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        pl_ace = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl_ace))
        self.assertNotIn("number_rooms", pl_ace.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        pl_ace = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl_ace))
        self.assertNotIn("number_bathrooms", pl_ace.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        pl_ace = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl_ace))
        self.assertNotIn("max_guest", pl_ace.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        pl_ace = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl_ace))
        self.assertNotIn("price_by_night", pl_ace.__dict__)

    def test_latitude_is_public_class_attribute(self):
        pl_ace = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl_ace))
        self.assertNotIn("latitude", pl_ace.__dict__)

    def test_longitude_is_public_class_attribute(self):
        pl_ace = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl_ace))
        self.assertNotIn("longitude", pl_ace.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        pl_ace = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl_ace))
        self.assertNotIn("amenity_ids", pl_ace.__dict__)

    def test_two_places_unique_ids(self):
        pl_ace1 = Place()
        pl_ace2 = Place()
        self.assertNotEqual(pl_ace1.id, pl_ace2.id)

    def test_two_places_different_created_at(self):
        pl_ace1 = Place()
        sleep(0.05)
        pl_ace2 = Place()
        self.assertLess(pl_ace1.created_at, pl_ace2.created_at)

    def test_two_places_different_updated_at(self):
        pl_ace1 = Place()
        sleep(0.05)
        pl_ace2 = Place()
        self.assertLess(pl_ace1.updated_at, pl_ace2.updated_at)

    def test_str_representation(self):
        date_time = datetime.today()
        dt_repr = repr(date_time)
        pl_ace = Place()
        pl_ace.id = "123456"
        pl_ace.created_at = pl_ace.updated_at = date_time
        plstr = pl_ace.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_args_unused(self):
        pl_ace = Place(None)
        self.assertNotIn(None, pl_ace.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_time = datetime.today()
        dt_iso = date_time.isoformat()
        pl_ace = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(pl_ace.id, "345")
        self.assertEqual(pl_ace.created_at, date_time)
        self.assertEqual(pl_ace.updated_at, date_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

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
        pl_ace = Place()
        sleep(0.05)
        first_updated_at = pl_ace.updated_at
        pl_ace.save()
        self.assertLess(first_updated_at, pl_ace.updated_at)

    def test_two_saves(self):
        pl_ace = Place()
        sleep(0.05)
        first_updated_at = pl_ace.updated_at
        pl_ace.save()
        second_updated_at = pl_ace.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        pl_ace.save()
        self.assertLess(second_updated_at, pl_ace.updated_at)

    def test_save_with_arg(self):
        pl_ace = Place()
        with self.assertRaises(TypeError):
            pl_ace.save(None)

    def test_save_updates_file(self):
        pl_ace = Place()
        pl_ace.save()
        plid = "Place." + pl_ace.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        pl_ace = Place()
        self.assertIn("id", pl_ace.to_dict())
        self.assertIn("created_at", pl_ace.to_dict())
        self.assertIn("updated_at", pl_ace.to_dict())
        self.assertIn("__class__", pl_ace.to_dict())

    def test_to_dict_contains_added_attributes(self):
        pl_ace = Place()
        pl_ace.middle_name = "ALX"
        pl_ace.my_number = 98
        self.assertEqual("ALX", pl_ace.middle_name)
        self.assertIn("my_number", pl_ace.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        pl_ace = Place()
        pl_dict = pl_ace.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        date_time = datetime.today()
        pl_ace = Place()
        pl_ace.id = "123456"
        pl_ace.created_at = pl_ace.updated_at = date_time
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(pl_ace.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        pl_ace = Place()
        self.assertNotEqual(pl_ace.to_dict(), pl_ace.__dict__)

    def test_to_dict_with_arg(self):
        pl_ace = Place()
        with self.assertRaises(TypeError):
            pl_ace.to_dict(None)


if __name__ == "__main__":
    unittest.main()
